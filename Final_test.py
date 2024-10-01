import os
import re
import json
import markdown2
from bs4 import BeautifulSoup
from tqdm import tqdm

# Extract the Foreword section from Markdown files
def extract_relevant_text_from_md(file_path, section_title="Foreword"):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    html_content = markdown2.markdown(md_content)
    soup = BeautifulSoup(html_content, 'html.parser')
    text = ""
    section_found = False
    for element in soup.stripped_strings:
        if section_title in element:
            section_found = True
        if section_found:
            text += element + "\n"
    return text.strip()

# Clean the extracted text
def clean_text(text):
    text = re.sub(r'[^\w\s\.\-]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Count the number of tables
def count_tables(text):
    return text.count('|')  # A simple heuristic method: count the '|' symbol to estimate tables

# Analyze the dataset, counting text blocks, size, number of tables, etc.
def analyze_dataset(dataset):
    total_chunks = len(dataset)
    total_size = sum(len(item['text']) for item in dataset)
    chunk_sizes = [len(item['text']) for item in dataset]
    total_tables = sum(count_tables(item['text']) for item in dataset)

    return {
        "total_chunks": total_chunks,
        "total_tables": total_tables,
        "total_size_bytes": total_size,
        "average_chunk_size_bytes": total_size / total_chunks if total_chunks > 0 else 0,
        "min_chunk_size_bytes": min(chunk_sizes) if chunk_sizes else 0,
        "max_chunk_size_bytes": max(chunk_sizes) if chunk_sizes else 0
    }

# Batch process Markdown files, chunking and cleaning them
def batch_process_md_files(root_dir, section_title="Foreword", chunk_size=512):
    dataset = []
    for subdir, dirs, files in tqdm(os.walk(root_dir), desc="Processing files"):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(subdir, file)
                text_data = extract_relevant_text_from_md(md_file_path, section_title)
                cleaned_text = clean_text(text_data)

                # Chunk processing
                chunks = [cleaned_text[i:i + chunk_size] for i in range(0, len(cleaned_text), chunk_size)]

                for i, chunk in enumerate(chunks):
                    dataset.append({
                        "id": f"{file}_{i}",
                        "text": chunk,
                        "metadata": {
                            "source": file,
                            "section": section_title,
                            "chunk_number": i
                        }
                    })

    return dataset

# Save the dataset as a JSON file
def save_dataset(dataset, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "processed_dataset.json")
    with open(output_file, "w", encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)
    print(f"Dataset saved to {output_file}")

# Generate a dataset description file
def generate_dataset_description(dataset_info, output_dir):
    description = f"""
    Dataset Description:
    This dataset consists of {dataset_info['total_chunks']} text chunks derived from 3GPP specification documents.
    The chunks contain extracted and processed content from the "Foreword" section of each document.
    The dataset includes approximately {dataset_info['total_tables']} tables, with a total size of {dataset_info['total_size_bytes'] / (1024 * 1024):.2f} MB.
    Chunk sizes range from {dataset_info['min_chunk_size_bytes'] / 1024:.2f} KB to {dataset_info['max_chunk_size_bytes'] / 1024:.2f} KB, with an average size of {dataset_info['average_chunk_size_bytes'] / 1024:.2f} KB.
    """

    description_file = os.path.join(output_dir, "dataset_description.txt")
    with open(description_file, "w", encoding='utf-8') as f:
        f.write(description)
    print(f"Dataset description saved to {description_file}")

# Main processing function, including dataset processing and analysis
def process_and_analyze(input_dir, output_dir, section_title="Foreword", chunk_size=512):
    print("Starting preprocessing...")
    dataset = batch_process_md_files(input_dir, section_title, chunk_size)
    print(f"Processed {len(dataset)} chunks.")

    save_dataset(dataset, output_dir)

    dataset_info = analyze_dataset(dataset)
    generate_dataset_description(dataset_info, output_dir)

    print("Preprocessing completed successfully.")
    return dataset, dataset_info

# Yixin_test:Call the function to process the folder
input_dir = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/21_series"
output_dir = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/cleaned_data"
process_and_analyze(input_dir, output_dir)