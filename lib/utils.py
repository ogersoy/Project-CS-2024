import os
from pathlib import Path
from transformers import AlbertTokenizer, AlbertModel, AlbertForSequenceClassification
from sklearn.metrics.pairwise import cosine_similarity
import torch
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader

# Import the clean_markdown function from your markdown_cleaner
from markdown_cleaner import clean_markdown


def load_and_clean_docs(directory):
    """Load and clean markdown documents from a directory."""
    directory = Path(directory)
    loader = DirectoryLoader(str(directory), glob="**/*.md")
    documents = loader.load()
    cleaned_docs = []
    for doc in documents:
        cleaned_content, _ = clean_markdown(doc.page_content)
        cleaned_docs.append(cleaned_content)
    return cleaned_docs

# def load_and_clean_docs(directory):
#     """Load and clean markdown documents from a directory."""
#     directory = Path(directory)
#     loader = DirectoryLoader(str(directory), glob="**/*.md")
#     documents = loader.load()
#     cleaned_docs = []
#     for doc in documents:
#         # Print the type of doc and its available attributes
#         print(f"Document: {doc}")
#         print(f"Document type: {type(doc)}")
#         print(f"Document attributes: {dir(doc)}")  # List all attributes of the object
#         cleaned_content, _ = clean_markdown(doc.page_content)  # Assuming page_content is an attribute containing the content
#         cleaned_docs.append(cleaned_content)
#     return cleaned_docs

def split_texts(texts, chunk_size=1000, chunk_overlap=200):
    """Split texts into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return text_splitter.split_documents(texts)

# Yixin
# Based on the compatibility of the LangChain version on my computer, I replaced `split_texts` with the `split_documents` method.


def setup_albert_models():
    """Set up ALBERT models for embedding and classification."""
    tokenizer = AlbertTokenizer.from_pretrained('albert-base-v2')
    embedding_model = AlbertModel.from_pretrained('albert-base-v2')
    classification_model = AlbertForSequenceClassification.from_pretrained('albert-base-v2', num_labels=3)
    return tokenizer, embedding_model, classification_model


def get_embedding(text, tokenizer, model):
    """Get ALBERT embedding for a given text."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()


def create_document_embeddings(chunks, tokenizer, model):
    """Create embeddings for all document chunks."""
    return [get_embedding(chunk, tokenizer, model) for chunk in chunks]


def find_most_relevant_chunk(query, chunks, doc_embeddings, tokenizer, model):
    """Find the most relevant chunk to the query using cosine similarity."""
    query_embedding = get_embedding(query, tokenizer, model)
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]
    most_relevant_idx = np.argmax(similarities)
    return chunks[most_relevant_idx]


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
    tokenizer, embedding_model, classification_model = setup_albert_models()
    doc_embeddings = create_document_embeddings(chunks, tokenizer, embedding_model)
    return chunks, doc_embeddings, tokenizer, embedding_model, classification_model


def answer_question(query, chunks, doc_embeddings, tokenizer, embedding_model, classification_model):
    """Answer a question using ALBERT embeddings and classification."""
    relevant_chunk = find_most_relevant_chunk(query, chunks, doc_embeddings, tokenizer, embedding_model)
    relevance = classify_relevance(query, relevant_chunk, tokenizer, classification_model)
    return relevant_chunk, relevance