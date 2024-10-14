import os
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import AlbertTokenizer, AlbertForSequenceClassification
import json

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
def train_model(md_folder_path, model_name='albert-base-v2', batch_size=16, epochs=3, learning_rate=2e-5):
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
    dataset = TextDataset(md_texts, tokenizer, max_len=512)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    print("Dataset and dataloader created.")

    # Load pre-trained Albert model
    print("Loading pre-trained Albert model...")
    model = AlbertForSequenceClassification.from_pretrained(model_name)
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    print("Model loaded.")

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    print(f"Using device: {device}")

    # Start training
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
            outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
            loss = outputs.loss

            # Backward
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

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
        options = [value.get(f'option_{i}') for i in range(1, 5) if value.get(f'option_{i}')]
        correct_answer = value['answer']
        qa_pairs.append({"question": question, "options": options, "correct_answer": correct_answer})

    # Generate answers
    for qa_pair in qa_pairs:
        question = qa_pair['question']
        options = qa_pair['options']
        correct_answer = qa_pair['correct_answer']

        # Prepare input for the model
        inputs = tokenizer(question, return_tensors='pt').to(device)
        outputs = model(**inputs)
        predicted_label = torch.argmax(outputs.logits, dim=1).item()

        # Print question, options, and predicted answer
        print(f"Question: {question}")
        for i, option in enumerate(options, 1):
            print(f"Option {i}: {option}")
        print(f"Predict: Answer {predicted_label + 1}")
        print(f"Correct Answer: {correct_answer}\n")

# Train the model
train_model("../cleaned_data")

# Evaluate the model
evaluate_model('./trained_albert', './trained_albert', '../Q-small_Sampled_3GPP_TR_Questions.json')