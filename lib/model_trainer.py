import os
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import AlbertTokenizer, AlbertForSequenceClassification
import json
import torch.nn as nn
from torch.cuda.amp import autocast, GradScaler


class AlbertBinaryClassifier(nn.Module):
    def __init__(self, model_name='albert-base-v2'):
        super(AlbertBinaryClassifier, self).__init__()
        self.albert = AlbertModel.from_pretrained(model_name)
        self.classifier = nn.Linear(self.albert.config.hidden_size, 1)  # Single output for binary classification

    def forward(self, input_ids, attention_mask):
        outputs = self.albert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs[1]  # Get the pooled output from Albert
        logits = self.classifier(pooled_output)
        return logits

# Load dataset
def read_md_files_from_folder(folder_path):
    md_files_content = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                md_files_content.append(f.read())

    return md_files_content

class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_len):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index):
        text = self.texts[index]
        inputs = self.tokenizer(text, max_length=self.max_len, padding='max_length', truncation=True, return_tensors="pt")
        return {
            'input_ids': inputs['input_ids'].squeeze(0),
            'attention_mask': inputs['attention_mask'].squeeze(0),
            'labels': torch.tensor(1)  # All inputs are positive
        }

# Step 3: Train model
def train_model(md_folder_path, model_name='albert-base-v2', batch_size=32, epochs=3, learning_rate=2e-5):
    # Load md files
    print("Loading markdown files...")
    md_texts = read_md_files_from_folder(md_folder_path)
    print(f"Loaded {len(md_texts)} markdown files.")

    # Load tokenizer
    print("Loading tokenizer...")
    tokenizer = AlbertTokenizer.from_pretrained(model_name)
    print("Tokenizer loaded.")

    # Create Dataset and Dataloader
    print("Creating dataset and dataloader...")
    dataset = TextDataset(md_texts, tokenizer, max_len=256)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=False, num_workers=14, pin_memory=True)
    print("Dataset and dataloader created.")

    # Load pre-trained Albert model
    print("Loading pre-trained Albert model...")
    model = AlbertForSequenceClassification.from_pretrained(model_name)
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    print("Model loaded.")

    # Set device
    device = torch.device("cuda")
    model.to(device)
    print(f"Using device: {device}")
    
    
    scaler = GradScaler()

    # Start training
    loss_fn = nn.BCEWithLogitsLoss()
    print("Starting training...")
    model.train()
    for epoch in range(epochs):
        epoch_loss = 0
        for batch_idx, batch in enumerate(dataloader, 0):
            if (batch_idx + 1) % 10 == 0 or batch_idx == 0:
                print(f"Processing batch {batch_idx + 1}/{len(dataloader)}...")
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            # Forward
            with torch.amp.autocast(device_type='cuda'):
                outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)  # Include labels here
                loss = outputs.loss  # Use the loss directly from the outputs
            
            # print(outputs)  # This will show you what is being returned by the model
            # print(f"Loss is {type(loss)}")  # Should output: <class 'torch.Tensor'>

            # Backward pass with gradient scaling
            scaler.scale(loss).backward()

            # Optimizer step with gradient scaling
            scaler.step(optimizer)
            scaler.update()
            optimizer.zero_grad()           # Clear gradients
            torch.cuda.empty_cache() #Very important, clearing the gpu cache to avoid running out of memory
            epoch_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs} finished with loss: {epoch_loss / len(dataloader)}")

    # Save model and tokenizer
    model.save_pretrained('./trained_albert')
    tokenizer.save_pretrained('./trained_albert')

    print("Model training finished and stored at './trained_albert'")

# Evaluation using QA pairs
def evaluate_model(model_path, tokenizer_path, json_file_path):
    # Load trained model and tokenizer
    print("Loading trained model and tokenizer for evaluation...")
    tokenizer = AlbertTokenizer.from_pretrained(tokenizer_path)
    model = AlbertForSequenceClassification.from_pretrained(model_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    # Load question and answer pairs
    with open(json_file_path, 'r', encoding='utf-8') as f:
        qa_data = json.load(f)
    print(f"Loaded {len(qa_data)} question and answer pairs.")

    qa_pairs = []
    for key, value in qa_data.items():
        question = value['question']
        options = [value.get(f'option_{i}') for i in range(1, 5) if value.get(f'option_{i}') is not None]
        correct_answer = value['answer']  # Correct answer in 'option_x: description' format
        qa_pairs.append({"question": question, "options": options, "correct_answer": correct_answer})

    # Track correct predictions
    correct_predictions = 0
    total_questions = len(qa_pairs)

    # Generate answers
    for qa_pair in qa_pairs:
        question = qa_pair['question']
        options = qa_pair['options']
        correct_answer = qa_pair['correct_answer']  # Example: 'option_2: 6.5 dB'

        # Extract correct option index from the correct_answer
        correct_answer_index = int(
            correct_answer.split(':')[0].split('_')[1])  # Extracts the option number from 'option_x'

        # Prepare input for the model
        inputs = tokenizer(question, return_tensors='pt').to(device)
        outputs = model(**inputs)
        predicted_label = torch.argmax(outputs.logits, dim=1).item() + 1  # Predicted option is 1-indexed

        # Check if the prediction is correct
        if predicted_label == correct_answer_index:
            correct_predictions += 1

        # Print question, options, and predicted answer
        print(f"Question: {question}")
        for i, option in enumerate(options, 1):
            print(f"Option {i}: {option}")
        print(f"Predicted Answer: {predicted_label}")
        print(f"Correct Answer: {correct_answer}\n")

    # Calculate and print accuracy
    accuracy = correct_predictions / total_questions * 100
    print(f"Evaluation completed. Accuracy: {accuracy:.2f}% ({correct_predictions}/{total_questions})")


# # Train the model
# if __name__ == "__main__":
#     torch.multiprocessing.set_start_method('spawn', force=True)  # To explicitly set the multiprocessing start method
#     train_model("../cleaned_data")

# Evaluate the model
evaluate_model('./trained_albert', './trained_albert', '../Q-small_Sampled_3GPP_TR_Questions.json')