import os
from pathlib import Path
from transformers import BertTokenizer, BertForSequenceClassification
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np
import torch  # Make sure torch is imported
from langchain.text_splitter import RecursiveCharacterTextSplitter
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

def setup_sentence_bert():
    """Set up Sentence-BERT for embedding."""
    model = SentenceTransformer('all-MiniLM-L6-v2')  # A smaller, faster, and effective model for document embeddings
    return model

def get_sentence_embedding(text, model):
    """Get Sentence-BERT embedding for a given text."""
    return model.encode([text])[0]
    
def create_document_embeddings(chunks, model):
    """Create embeddings for all document chunks using Sentence-BERT."""
    return [get_sentence_embedding(chunk.page_content, model) for chunk in chunks]

def find_most_relevant_chunk(query, chunks, doc_embeddings, model):
    """Find the most relevant chunk to the query using cosine similarity."""
    query_embedding = get_sentence_embedding(query, model)
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    most_relevant_idx = np.argmax(similarities)
    return chunks[most_relevant_idx].page_content

def classify_relevance(query, context, tokenizer, model):
    """Classify the relevance of the context to the query."""
    inputs = tokenizer(query, context, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():  # Use torch's no_grad to avoid gradient computation
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = logits.argmax().item()
    
    classes = ["unrelated", "partially related", "fully answers the question"]
    return classes[predicted_class]

def process_documents(input_path):
    """Process documents and return necessary components for the chatbot."""
    cleaned_docs = load_and_clean_docs(input_path)
    chunks = split_texts(cleaned_docs)
    
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')  # Keep for classification
    classification_model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3)
    embedding_model = setup_sentence_bert()  # Switch to Sentence-BERT for better embeddings
    
    return chunks, tokenizer, embedding_model, classification_model

def answer_question(query, chunks, doc_embeddings, tokenizer, embedding_model, classification_model):
    """Answer a question using Sentence-BERT embeddings and classification."""
    relevant_chunk = find_most_relevant_chunk(query, chunks, doc_embeddings, embedding_model)
    return relevant_chunk  # Ensure this is just the relevant text

