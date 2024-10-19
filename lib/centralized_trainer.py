import os
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from torch.amp import autocast, GradScaler
from transformers import T5Tokenizer, T5ForConditionalGeneration
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

# Custom Dataset class with paper content
class ParagraphDataset(Dataset):
    def __init__(self, paragraphs, tokenizer, max_len):
        self.paragraphs = paragraphs  # Paper sections or paragraphs
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.paragraphs)

    def __getitem__(self, index):
        paragraph = self.paragraphs[index]
        input_text = f"context: {paragraph}"
        inputs = self.tokenizer(input_text, max_length=self.max_len, padding='max_length', truncation=True,
                                return_tensors="pt")

        return {
            'input_ids': inputs['input_ids'].squeeze(0),
            'attention_mask': inputs['attention_mask'].squeeze(0),
            'labels': inputs['input_ids'].squeeze(0)
        }

# Train model with paper content
def train_model(md_folder_path, model_name='t5-small', batch_size=32, epochs=3, learning_rate=2e-5):
    # Load dataset
    print("Loading dataset...")
    paragraphs = read_md_files_from_folder(md_folder_path)

    # Load tokenizer
    print("Loading tokenizer...")
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    print("Tokenizer loaded.")

    # Create Dataset for training
    print("Creating training dataset...")
    train_dataset = ParagraphDataset(paragraphs, tokenizer, max_len=256)
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)

    # Load pre-trained T5 model
    print("Loading pre-trained T5 model...")
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    print(f"Using device: {device}")
    optimizer = AdamW(model.parameters(), lr=learning_rate)
    scaler = GradScaler()
    print("Model loaded.")

    # Start training
    print("Starting training...")
    model.train()
    accumulation_steps = 4

    for epoch in range(epochs):
        epoch_loss = 0
        for batch_idx, batch in enumerate(train_dataloader):
            if (batch_idx + 1) % 10 == 0 or batch_idx == 0:
                print(f"Processing batch {batch_idx + 1}/{len(train_dataloader)}...")
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)

            # Forward pass with mixed precision using autocast
            with autocast(device_type='cuda'):
                outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss / accumulation_steps

            # Backward pass with scaled loss
            scaler.scale(loss).backward()

            if (batch_idx + 1) % accumulation_steps == 0:
                # Update weights and scale gradients
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad()

            epoch_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs} finished with loss: {epoch_loss / len(train_dataloader)}")

    # Save model and tokenizer
    model.save_pretrained('./trained_t5')
    tokenizer.save_pretrained('./trained_t5')
    print("Model training finished and stored at './trained_t5'")

    return model, tokenizer

# Evaluate the model on question-answer pairs from JSON
def evaluate_model(model, tokenizer, qa_file_path):
    # Load trained model and tokenizer
    print("Starting evaluation on test data...")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()

    # Load question and answer pairs from JSON
    with open(qa_file_path, 'r', encoding='utf-8') as f:
        qa_data = json.load(f)

    questions = [item['question'] for item in qa_data.values()]
    answers = [item['answer'] for item in qa_data.values()]

    correct_predictions = 0
    total_questions = len(questions)

    # Iterate over each question in the test set
    for idx, question in enumerate(questions):
        correct_answer = answers[idx]

        # Tokenize the question and generate the answer
        inputs = tokenizer.encode(f"question: {question} </s>", return_tensors='pt').to(device)
        outputs = model.generate(inputs, max_length=50)
        generated_answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Print question and generated answer
        print(f"Question: {question}")
        print(f"Generated Answer: {generated_answer}")
        print(f"Correct Answer: {correct_answer}")

        # Compare generated answer with correct answer
        if generated_answer.strip().lower() == correct_answer.strip().lower():
            correct_predictions += 1

    # Calculate and print accuracy
    accuracy = correct_predictions / total_questions * 100
    print(f"Evaluation completed. Accuracy: {accuracy:.2f}% ({correct_predictions}/{total_questions})")

# Example to call functions
if __name__ == "__main__":
    #model, tokenizer = train_model("../cleaned_data")
    model=T5ForConditionalGeneration.from_pretrained("./trained_t5")
    tokenizer=T5Tokenizer.from_pretrained("./trained_t5")
    evaluate_model(model=model,tokenizer=tokenizer, qa_file_path="../Q-small_Sampled_3GPP_TR_Questions.json")