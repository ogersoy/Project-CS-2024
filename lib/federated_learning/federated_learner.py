import os
import torch
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from transformers import AlbertTokenizer, AlbertForSequenceClassification
import json
import flwr as fl

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

# Flower client for federated learning
class FlowerClient(fl.client.NumPyClient):
    def __init__(self, model, train_loader, device):
        self.model = model
        self.train_loader = train_loader
        self.device = device
        self.optimizer = AdamW(model.parameters(), lr=2e-5)

    def get_parameters(self, config=None):
        print("Getting model parameters - start")
        params = [val.cpu().numpy() for _, val in self.model.state_dict().items()]
        print(f"Model parameters obtained: {len(params)} layers")
        return params

    def set_parameters(self, parameters):
        print("Setting model parameters - start")
        params_dict = zip(self.model.state_dict().keys(), parameters)
        state_dict = {k: torch.tensor(v) for k, v in params_dict}
        self.model.load_state_dict(state_dict, strict=True)
        print("Model parameters set - completed")

    def fit(self, parameters, config):
        print("Starting training round - received parameters")
        self.set_parameters(parameters)
        self.model.train()

        for epoch in range(1):
            print(f"Training epoch {epoch + 1}")  # Just one epoch per round
            for batch_idx, batch in enumerate(self.train_loader):
                print(f"Processing batch {batch_idx + 1}/{len(self.train_loader)}")
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)

                # Forward
                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss

                # Backward
                loss.backward()
                self.optimizer.step()
                self.optimizer.zero_grad()

        return self.get_parameters(), len(self.train_loader.dataset), {}

    def evaluate(self, parameters, config):
        print("Evaluating model")
        self.set_parameters(parameters)
        self.model.eval()
        return 0.0, len(self.train_loader.dataset), {}

# Prepare model, dataset and client
model_name = 'albert-base-v2'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AlbertForSequenceClassification.from_pretrained(model_name).to(device)
tokenizer = AlbertTokenizer.from_pretrained(model_name)
md_texts = read_md_files_from_folder("../../cleaned_data")
dataset = TextDataset(md_texts, tokenizer, max_len=512)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

# Start Flower client
client = FlowerClient(model, dataloader, device)
fl.client.start_client(server_address="127.0.0.1:8080", client=client.to_client())

# Evaluation function
def evaluate_model(model, tokenizer, json_file_path, device):
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

# Evaluate model
evaluate_model(model, tokenizer, '../../Q-small_Sampled_3GPP_TR_Questions.json', device)