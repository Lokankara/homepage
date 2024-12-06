import os
import re

def convert_md_to_html(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    html_content = ""

    # Convert headers
    html_content += re.sub(r"^# (.*?)$", r"<h1>\1</h1>", md_content, flags=re.MULTILINE)
    html_content += re.sub(r"^## (.*?)$", r"<h2>\1</h2>", md_content, flags=re.MULTILINE)
    html_content += re.sub(r"^### (.*?)$", r"<h3>\1</h3>", md_content, flags=re.MULTILINE)

    # Convert code blocks (inline code and multiline code blocks)
    html_content = re.sub(r"`(.*?)`", r"<code>\1</code>", html_content)  # Inline code
    html_content = re.sub(r"```\s*(.*?)\s*```", r"<pre><code>\1</code></pre>", html_content, flags=re.DOTALL)  # Code blocks

    # Convert images
    html_content = re.sub(r"!\[.*?\]\((.*?)\)", r'<img src="\1" alt="image">', html_content)

    # Convert paragraphs (simplified)
    html_content = re.sub(r"^(?!<)([^\n]+)", r"<p>\1</p>", html_content, flags=re.MULTILINE)

    # Add line breaks for Markdown line breaks
    html_content = html_content.replace("\n", "<br>")

    return html_content

def process_directory(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for md_file in filenames:
            if md_file.endswith('.md'):
                md_file_path = os.path.join(dirpath, md_file)
                html_content = convert_md_to_html(md_file_path)
                html_file_path = md_file_path.replace('.md', '.html')

                with open(html_file_path, 'w', encoding='utf-8') as html_file:
                    html_file.write(html_content)

root_folder = '/'
process_directory(root_folder)

print("All Markdown files have been converted to HTML!")
