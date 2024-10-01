import os
import re
import markdown2
from bs4 import BeautifulSoup
import pandas as pd


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


def clean_text(text):
    text = re.sub(r'[^\w\s\.\-]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def save_to_txt(text_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_data)


def count_tables(text):
    return text.count('|')  # Simple heuristic: count vertical bars as potential table delimiters


def analyze_dataset(root_dir):
    total_files = 0
    total_tables = 0
    total_size = 0
    file_sizes = []

    for subdir, dirs, files in os.walk(os.path.join(root_dir, 'cleaned')):
        for file in files:
            if file.endswith(".txt"):
                total_files += 1
                file_path = os.path.join(subdir, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    size = len(content)
                    total_size += size
                    file_sizes.append(size)
                    total_tables += count_tables(content)

    avg_size = total_size / total_files if total_files > 0 else 0
    return {
        "total_files": total_files,
        "total_tables": total_tables,
        "total_size_bytes": total_size,
        "average_file_size_bytes": avg_size,
        "min_file_size_bytes": min(file_sizes) if file_sizes else 0,
        "max_file_size_bytes": max(file_sizes) if file_sizes else 0
    }


def batch_process_md_files(root_dir, section_title="Foreword"):
    processed_files = 0
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(subdir, file)
                text_data = extract_relevant_text_from_md(md_file_path, section_title)
                cleaned_text = clean_text(text_data)
                relative_path = os.path.relpath(subdir, root_dir)
                output_dir = os.path.join(root_dir, 'cleaned', relative_path)
                os.makedirs(output_dir, exist_ok=True)
                txt_file_path = os.path.join(output_dir, file.replace(".md", ".txt"))
                save_to_txt(cleaned_text, txt_file_path)
                processed_files += 1
                print(f"Processed {md_file_path} and saved to {txt_file_path}")
    return processed_files


def process_and_analyze(root_dir, section_title="Foreword"):
    processed_files = batch_process_md_files(root_dir, section_title)
    print(f"Processed {processed_files} files.")

    dataset_info = analyze_dataset(root_dir)

    description = f"""
    Dataset Description:
    This dataset consists of {dataset_info['total_files']} cleaned text files derived from 3GPP specification documents.
    The files contain extracted and processed content from the "{section_title}" section of each document.
    The dataset includes approximately {dataset_info['total_tables']} tables, with a total size of {dataset_info['total_size_bytes'] / (1024 * 1024):.2f} MB.
    File sizes range from {dataset_info['min_file_size_bytes'] / 1024:.2f} KB to {dataset_info['max_file_size_bytes'] / 1024:.2f} KB, with an average size of {dataset_info['average_file_size_bytes'] / 1024:.2f} KB.
    """

    # Save the description to a file
    with open(os.path.join(root_dir, "dataset_description.txt"), "w") as f:
        f.write(description)

    return dataset_info, description

# Example usage:
# import preprocess.py
# info, desc = preprocess.process_and_analyze("path/to/your/data")
# print(desc)

# Yixin test
# root_dir = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/21_series"
# section_title = "Foreword"
# process_and_analyze(root_dir, section_title)