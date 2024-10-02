import os
import re
import markdown
from bs4 import BeautifulSoup
import html2text
import pandas as pd
from pathlib import Path

def remove_glossary(content):
    pattern = re.compile(r'Glossary.*?(?=\n\s*\n)', re.DOTALL | re.IGNORECASE)
    return re.sub(pattern, '', content)

def remove_header_footer(content):
    lines = content.split('\n')
    # Remove header (first 5 lines)
    lines = lines[5:]
    # Remove footer (last 5 lines)
    lines = lines[:-5]
    return '\n'.join(lines)

def process_tables(soup):
    tables = []
    for table in soup.find_all('table'):
        df = pd.read_html(str(table))[0]
        tables.append(df)
    return tables

def remove_images(soup):
    for img in soup.find_all('img'):
        img.decompose()

def remove_links(soup):
    for a in soup.find_all('a'):
        a.replace_with(a.text)

def clean_markdown(content):
    # Remove header and footer
    content = remove_header_footer(content)
    # Remove glossary
    content = remove_glossary(content)
    
    html = markdown.markdown(content)
    soup = BeautifulSoup(html, 'html.parser')
    
    # Process tables
    tables = process_tables(soup)
    
    remove_images(soup)
    remove_links(soup)
    cleaned_html = str(soup)
    
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = False  # Keep tables
    cleaned_md = h.handle(cleaned_html)
    
    cleaned_md = re.sub(r'\n{3,}', '\n\n', cleaned_md)
    cleaned_md = re.sub(r'<[^>]+>', '', cleaned_md)
    cleaned_md = '\n'.join([line for line in cleaned_md.split('\n') if line.strip()])
    
    return cleaned_md, tables

def process_file(input_path, output_path):
    with input_path.open('r', encoding='utf-8') as file:
        content = file.read()
    
    original_size = len(content)
    cleaned_content, tables = clean_markdown(content)
    cleaned_size = len(cleaned_content)
    
    with output_path.open('w', encoding='utf-8') as file:
        file.write(cleaned_content)
    
    file_info = {
        'original_size': original_size,
        'cleaned_size': cleaned_size,
        'num_tables': len(tables),
        'tables': tables
    }
    
    return file_info

def process_directory(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    processed_files = []
    dataset_info = {
        'total_files': 0,
        'total_original_size': 0,
        'total_cleaned_size': 0,
        'total_tables': 0,
        'files': {}
    }
    
    for file_path in input_dir.glob('*.md'):
        output_path = output_dir / file_path.name
        
        file_info = process_file(file_path, output_path)
        dataset_info['files'][file_path.name] = file_info
        
        dataset_info['total_files'] += 1
        dataset_info['total_original_size'] += file_info['original_size']
        dataset_info['total_cleaned_size'] += file_info['cleaned_size']
        dataset_info['total_tables'] += file_info['num_tables']
        
        processed_files.append(file_path.name)
    
    return dataset_info

def generate_dataset_summary(dataset_info):
    summary = f"Dataset Summary:\n"
    summary += f"Total number of files: {dataset_info['total_files']}\n"
    summary += f"Total original size: {dataset_info['total_original_size']} bytes\n"
    summary += f"Total cleaned size: {dataset_info['total_cleaned_size']} bytes\n"
    summary += f"Total number of tables: {dataset_info['total_tables']}\n\n"
    
    summary += "File Details:\n"
    for filename, file_info in dataset_info['files'].items():
        summary += f"  {filename}:\n"
        summary += f"    Original size: {file_info['original_size']} bytes\n"
        summary += f"    Cleaned size: {file_info['cleaned_size']} bytes\n"
        summary += f"    Number of tables: {file_info['num_tables']}\n"
        for i, table in enumerate(file_info['tables']):
            summary += f"      Table {i+1} shape: {table.shape}\n"
        summary += "\n"
    
    return summary

# Example usage
input_directory = Path("/mnt/c/Users/Mahta/projectcs/TSpec-LLM/test")
output_directory = Path("/mnt/c/Users/Mahta/projectcs/TSpec-LLM/testcleaned")
dataset_info = process_directory(input_directory, output_directory)

# Generate and print the dataset summary
summary = generate_dataset_summary(dataset_info)
print(summary)

# Optionally, save the summary to a file
with open(output_directory / 'dataset_summary.txt', 'w', encoding='utf-8') as f:
    f.write(summary)