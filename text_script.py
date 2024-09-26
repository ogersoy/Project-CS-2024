from http.client import responses
from docx import Document
from datasets import load_dataset
from huggingface_hub import login
import requests
from io import BytesIO

# Load and read the file
def load_docx(file):
    doc = Document(file)
    content = []  # To store paragraphs in sequence
    start_extracting = False  # Flag to start extracting content after '1 Scope'

    # Loop through the document element by element
    for para in doc.paragraphs:
        text = para.text.strip()

        # Check if 'Scope' is found, and start extracting content from this point onwards
        if "Scope" in text:
            start_extracting = True  # Start extracting content from this point
            content.append(text)  # Append '1 Scope' to content
            continue

        # If we haven't found 'Scope' yet, skip the content
        if not start_extracting:
            continue

        # Extract and append all paragraphs after '1 Scope'
        if start_extracting and text:
            content.append(text)

    return '\n'.join(content)

# Fetch docx from HuggingFace
api_token="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"
url="https://huggingface.co/datasets/rasoul-nikbakht/TSpec-LLM/resolve/main/3GPP-clean/Rel-14/29_series/29061-e40.docx"
headers={
    "Authorization":f"Bearer {api_token}"
}
response=requests.get(url,headers=headers)

doc = BytesIO(response.content)

print(load_docx(doc))