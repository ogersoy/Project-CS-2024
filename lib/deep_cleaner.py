import re
import os

def deep_cleaner(content):
    # Find and remove sections starting with "##### Change history"
    sections = re.split(r"(##### .*?\n)", content, flags=re.IGNORECASE)  # Split content by each section heading (##### level)

    cleaned_content = ""
    skip_section = False

    for i in range(len(sections)):
        section = sections[i]
        if re.match(r"##### .*Change history.*", section, re.IGNORECASE):
            # If this section is a "##### Change history" (ignoring case), skip this section
            skip_section = True
        elif section.startswith("##### "):
            # If it's a different section, stop skipping
            skip_section = False

        if not skip_section:
            cleaned_content += section

    return cleaned_content.strip()

# Define the function to process all .md files in the directory and its subdirectories
def process_md_files(root_directory, output_directory):
    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".md"):
                # Construct the input file path
                file_path = os.path.join(root, file)

                # Calculate the relative path from the root directory
                relative_path = os.path.relpath(root, root_directory)

                # Construct the output file path, preserving directory structure
                output_dir_path = os.path.join(output_directory, relative_path)
                os.makedirs(output_dir_path, exist_ok=True)

                output_file_path = os.path.join(output_dir_path, file)

                # Read the content of the file
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        file_content = f.read()
                except UnicodeDecodeError:
                    # If utf-8 fails, try 'latin1' or another common encoding
                    with open(file_path, "r", encoding="latin1") as f:
                        file_content = f.read()

                # Clean the file content
                cleaned_content = deep_cleaner(file_content)

                # Save the cleaned content to the new file in the output directory
                with open(output_file_path, "w", encoding="utf-8") as output_file:
                    output_file.write(cleaned_content)

                print(f"Cleaned content saved to: {output_file_path}")

def delete_empty_md_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) == 0:
                    os.remove(file_path)
                    print(f"Deleted empty file: {file_path}")


def summarize_folder_info(root_directory):
    file_count = 0
    total_size = 0

    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".md"):
                file_count += 1
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)

    # Convert total size to MB
    total_size_mb = total_size / (1024 * 1024)

    print(f"Total number of .md files: {file_count}")
    print(f"Total size of .md files: {total_size_mb:.2f} MB")


root_directory = "C:/Users/Administrator/Desktop/cleaned_data"
output_directory= "C:/Users/Administrator/Desktop/cleaned_data1"
#process_md_files(root_directory,output_directory)
#delete_empty_md_files(root_directory)
summarize_folder_info(root_directory)