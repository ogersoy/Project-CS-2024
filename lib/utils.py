import os
from pathlib import Path
from transformers import BertTokenizer, BertModel, BertForSequenceClassification
from sklearn.metrics.pairwise import cosine_similarity
import torch
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Import the process_file function from your markdown_cleaner
from lib.markdown_cleaner import process_file

def load_and_clean_docs(directory):
    """Load and clean markdown documents from a directory."""
    directory = Path(directory)
    cleaned_docs = []
    for file_path in directory.glob('**/*.md'):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        cleaned_content, _ = process_file(content)
        cleaned_docs.append(cleaned_content)
    return cleaned_docs

def split_texts(texts, chunk_size=1000, chunk_overlap=200):
    """Split texts into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return text_splitter.create_documents(texts)

def setup_bert_models():
    """Set up BERT models for embedding and classification."""
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    embedding_model = BertModel.from_pretrained('bert-base-uncased')
    classification_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
    return tokenizer, embedding_model, classification_model

def get_embedding(text, tokenizer, model):
    """Get BERT embedding for a given text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def create_document_embeddings(chunks, tokenizer, model):
    """Create embeddings for all document chunks."""
    return [get_embedding(chunk.page_content, tokenizer, model) for chunk in chunks]

def find_most_relevant_chunk(query, chunks, doc_embeddings, tokenizer, model):
    """Find the most relevant chunk to the query using cosine similarity."""
    query_embedding = get_embedding(query, tokenizer, model)
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    most_relevant_idx = np.argmax(similarities)
    return chunks[most_relevant_idx].page_content

def classify_relevance(query, context, tokenizer, model):
    """Classify the relevance of the context to the query."""
    inputs = tokenizer(query, context, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()
    
    classes = ["unrelated", "partially related", "fully answers the question"]
    return classes[predicted_class]

def process_documents(input_path):
    """Process documents and return necessary components for the chatbot."""
    cleaned_docs = load_and_clean_docs(input_path)
    chunks = split_texts(cleaned_docs)
    tokenizer, embedding_model, classification_model = setup_bert_models()
    doc_embeddings = create_document_embeddings(chunks, tokenizer, embedding_model)
    return chunks, doc_embeddings, tokenizer, embedding_model, classification_model

def answer_question(query, chunks, doc_embeddings, tokenizer, embedding_model, classification_model):
    """Answer a question using BERT embeddings and classification."""
    relevant_chunk = find_most_relevant_chunk(query, chunks, doc_embeddings, tokenizer, embedding_model)
    relevance = classify_relevance(query, relevant_chunk, tokenizer, classification_model)
    return relevant_chunk, relevance