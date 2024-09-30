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
    text = re.sub(r'[^\w\s\.\-\|]', '', text)  # Keep decimal points, "-", and other useful characters like "|"
    text = re.sub(r'\s+', ' ', text)  # Clean up extra whitespace
    return text.strip()


# Extract and properly handle table content while preserving the table format
def extract_tables_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Regular expression to find Markdown tables
    table_pattern = re.compile(r'(\|.+?\|)', re.DOTALL)
    tables = table_pattern.findall(md_content)

    cleaned_tables = []
    if tables:
        for table in tables:
            rows = table.strip().split('\n')
            table_data = []
            for row in rows:
                if '|' in row:
                    columns = row.split('|')[1:-1]  # Ignore the leading and trailing '|'
                    cleaned_row = [col.strip() for col in columns]
                    table_data.append(cleaned_row)
            cleaned_tables.append(table_data)
    else:
        print("No tables found in the document.")

    return cleaned_tables


# Save the processed data to a TXT file while preserving the table format
def save_to_txt(text_data, table_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Text Data:\n")
        f.write(text_data)
        f.write("\n\nTable Data:\n")

        for table in table_data:
            f.write("Table Start:\n")
            for row in table:
                f.write("\t".join(row) + "\n")
            f.write("Table End:\n\n")


# Main program: Extract, clean, process, and save data
def main_md(file_path, output_file):
    # Extract the specified section from the Markdown text
    text_data = extract_relevant_text_from_md(file_path, section_title="5 Specifications and Reports")

    # Clean the text content, preserving decimal points and "-" symbols
    cleaned_text = clean_text(text_data)

    # Extract and clean table content while preserving the table format
    table_data = extract_tables_from_md(file_path)

    # Save as TXT
    save_to_txt(cleaned_text, table_data, output_file)
    print(f"Markdown data has been successfully extracted and saved as {output_file}")


# Execute the code
file_path = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8/21_series/21101-840.md"  # Replace with the path to your Markdown file
output_file = "cleaned_md_data1.txt"
main_md(file_path, output_file)
