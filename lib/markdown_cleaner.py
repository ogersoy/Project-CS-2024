import os
import re
import markdown
from bs4 import BeautifulSoup
import html2text

def remove_paragraph_with_style(content, style_value):
    lines = content.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith(style_value)]
    return '\n'.join(cleaned_lines)

def remove_section(content, section_title):
    pattern = re.compile(f'{re.escape(section_title)}.*?(?=\n\s*\n)', re.DOTALL | re.IGNORECASE)
    return re.sub(pattern, '', content)

def remove_header_footer(content):
    lines = content.split('\n')
    # Remove header (first 5 lines)
    lines = lines[5:]
    # Remove footer (last 5 lines)
    lines = lines[:-5]
    return '\n'.join(lines)

def remove_tables(soup):
    for table in soup.find_all('table'):
        table.decompose()

def remove_images(soup):
    for img in soup.find_all('img'):
        img.decompose()

def remove_links(soup):
    for a in soup.find_all('a'):
        a.replace_with(a.text)

def remove_figure_references(content):
    return re.sub(r'^.*Figure\s+\d+.*$', '', content, flags=re.MULTILINE)

def clean_markdown(content):
    # Remove header and footer
    content = remove_header_footer(content)
    # Remove specific sections
    content = remove_section(content, "Contents")
    content = remove_paragraph_with_style(content, "Instructions")
    content = remove_figure_references(content)
    
    html = markdown.markdown(content)
    soup = BeautifulSoup(html, 'html.parser')
    remove_tables(soup)
    remove_images(soup)
    remove_links(soup)
    cleaned_html = str(soup)
    
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_tables = True
    cleaned_md = h.handle(cleaned_html)
    
    cleaned_md = re.sub(r'\n{3,}', '\n\n', cleaned_md)
    cleaned_md = re.sub(r'<[^>]+>', '', cleaned_md)
    cleaned_md = '\n'.join([line for line in cleaned_md.split('\n') if line.strip()])
    
    return cleaned_md

def process_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    processed_files = []
    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            with open(input_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            cleaned_content = clean_markdown(content)
            
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
            
            processed_files.append(filename)
    
    return processed_files
