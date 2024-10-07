import re
import markdown
from bs4 import BeautifulSoup
import html2text
import pandas as pd
from io import StringIO

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
        df = pd.read_html(StringIO(str(table)))[0]
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

def process_file(content):
    original_size = len(content)
    cleaned_content, tables = clean_markdown(content)
    cleaned_size = len(cleaned_content)
    
    file_info = {
        'original_size': original_size,
        'cleaned_size': cleaned_size,
        'num_tables': len(tables),
        'tables': tables
    }
    
    return cleaned_content, file_info