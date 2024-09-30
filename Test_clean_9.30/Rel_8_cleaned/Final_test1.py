import os
import re
import markdown2
from bs4 import BeautifulSoup


# 1. 从Markdown文件中提取指定部分的文本
def extract_relevant_text_from_md(file_path, section_title="5 Specifications and Reports"):
    with open(file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 将Markdown转换为HTML
    html_content = markdown2.markdown(md_content)
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取指定章节的内容
    text = ""
    section_found = False
    for element in soup.stripped_strings:
        if section_title in element:
            section_found = True
        if section_found:
            text += element + "\n"

    return text.strip()


# 2. 清理文本内容，保留小数点和 "-" 符号
def clean_text(text):
    # 保留小数点和 "-" 符号
    text = re.sub(r'[^\w\s\.\-]', '', text)  # 仅移除不需要的特殊字符，保留小数点和"-"
    text = re.sub(r'\s+', ' ', text)  # 清理多余的空白符
    return text.strip()


# 3. 将处理后的数据保存为TXT
def save_to_txt(text_data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text_data)


# 4. 批量处理Markdown文件并生成对应的TXT文件
def batch_process_md_files(root_dir, section_title="5 Specifications and Reports"):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                md_file_path = os.path.join(subdir, file)

                # 提取Markdown文本的指定部分
                text_data = extract_relevant_text_from_md(md_file_path, section_title)

                # 清理文本内容，保留小数点和 "-" 符号
                cleaned_text = clean_text(text_data)

                # 构建输出目录和文件名
                relative_path = os.path.relpath(subdir, root_dir)  # 获取相对路径
                output_dir = os.path.join(root_dir, 'cleaned', relative_path)  # 构建清洗后的目录
                os.makedirs(output_dir, exist_ok=True)  # 创建目录
                txt_file_path = os.path.join(output_dir, file.replace(".md", ".txt"))

                # 保存为TXT
                save_to_txt(cleaned_text, txt_file_path)
                print(f"Processed {md_file_path} and saved to {txt_file_path}")


# 主程序：处理整个Rel-8目录下的所有Markdown文件
root_dir = "D:/Python/TsLLM/TSpec-LLM/3GPP-clean/Rel-8"  # 替换为你的根目录路径
batch_process_md_files(root_dir)
