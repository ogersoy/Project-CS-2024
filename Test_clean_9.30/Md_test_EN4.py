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

# Main function: Extract, clean, process, and save data
def main_md(file_path, output_file):
    # Extract the specified section from the Markdown text
    text_data = extract_relevant_text_from_md(file_path, section_title="5 Specifications and Reports")

    # Clean the text content, preserving decimal points and "-" symbols
    cleaned_text = clean_text(text_data)

    # Save as TXT
    save_to_txt(cleaned_text, output_file)
    print(f"Markdown data has been successfully extracted and saved as {output_file}")

# Execute the code
file_path = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/21_series/21101-840.md"  # Replace with your Markdown file path
output_file = "cleaned_md_data4.txt"
main_md(file_path, output_file)
