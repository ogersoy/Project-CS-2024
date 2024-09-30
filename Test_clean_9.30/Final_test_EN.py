import os
import re
import markdown2
from bs4 import BeautifulSoup

# 1. Extract specific section text from the Markdown file
def extract_relevant_text_from_md(file_path, section_title="5 Specifications and Reports"):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown2.markdown(md_content)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract the content of the specified section
    text = ""
    section_found = False
    for element in soup.stripped_strings:
        if section_title in element:
            section_found = True
        if section_found:
            text += element + "\n"

    return text.strip()

# 2. Clean the text content, preserving decimal points and "-" symbols
def clean_text(text):
    # Preserve decimal points and "-" symbols
    text = re.sub(r'[^\w\s\.\-]', '', text)  # Remove unwanted special characters, keep decimal points and "-"
    text = re.sub(r'\s+', ' ', text)  # Clean up extra whitespace
    return text.strip()

# 3. Save the processed data to a TXT file
def save_to_txt(text_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_data)

# 4. Batch process Markdown files and generate corresponding TXT files
def batch_process_md_files(root_dir, section_title="5 Specifications and Reports"):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(subdir, file)

                # Extract the specified section from the Markdown text
                text_data = extract_relevant_text_from_md(md_file_path, section_title)

                # Clean the text content, preserving decimal points and "-" symbols
                cleaned_text = clean_text(text_data)

                # Build output directory and file name
                relative_path = os.path.relpath(subdir, root_dir)  # Get relative path
                output_dir = os.path.join(root_dir, 'cleaned', relative_path)  # Build cleaned directory
                os.makedirs(output_dir, exist_ok=True)  # Create directory
                txt_file_path = os.path.join(output_dir, file.replace(".md", ".txt"))

                # Save as TXT
                save_to_txt(cleaned_text, txt_file_path)
                print(f"Processed {md_file_path} and saved to {txt_file_path}")

# Main program: Process all Markdown files under the Rel-8 directory
root_dir = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8"  # Replace with your root directory path
batch_process_md_files(root_dir)
