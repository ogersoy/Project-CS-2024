import re


# Extract specific section text from the Markdown file
def extract_relevant_text_from_md(file_path, section_title="5 Specifications and Reports"):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Extract the content of the specified section
    text = ""
    section_found = False
    for line in md_content.splitlines():
        if section_title in line:
            section_found = True
        if section_found:
            text += line + "\n"

    return text.strip()


# Clean the text content, preserving decimal points and "-" symbols
def clean_text(text):
    text = re.sub(r'[^\w\s\.\-\|]', '', text)  # Preserve decimal points, "-", "|" and other useful characters
    text = re.sub(r'\s+', ' ', text)  # Clean up extra whitespace
    return text.strip()


# Extract and properly handle table content while preserving the table format
def extract_tables_from_md(text):
    table_pattern = re.compile(r'(\|.+?\|)', re.DOTALL)
    lines = text.splitlines()
    cleaned_data = ""
    in_table = False

    for line in lines:
        if table_pattern.match(line):
            if not in_table:
                cleaned_data += "--Table Start--\n"
                in_table = True
            cleaned_data += line + "\n"
        else:
            if in_table:
                cleaned_data += "--Table End--\n"
                in_table = False
            cleaned_data += line + "\n"

    # If the table was not closed at the end
    if in_table:
        cleaned_data += "--Table End--\n"

    return cleaned_data


# Save the processed data to a TXT file, differentiating table and text data
def save_to_txt(cleaned_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_data)


# Main program: Extract, clean, process, and save data
def main_md(file_path, output_file):
    # Extract the specified section from the Markdown text
    raw_text = extract_relevant_text_from_md(file_path, section_title="5 Specifications and Reports")

    # Clean the text content, preserving decimal points and "-" symbols
    cleaned_text = clean_text(raw_text)

    # Extract and process table content
    processed_data = extract_tables_from_md(raw_text)

    # Save as TXT
    save_to_txt(processed_data, output_file)
    print(f"Markdown data has been successfully extracted and saved as {output_file}")


# Execute the code
file_path = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/21_series/21101-840.md"  # Replace with your Markdown file path
output_file = "cleaned_md_data2.txt"
main_md(file_path, output_file)
