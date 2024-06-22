from os.path import isfile
from block_markdown import block_to_block_type, get_header_html, markdown_to_html
from textnode import *
from htmlnode import *
from markdown import *
from block_markdown import *

import os
import sys
import shutil
def main():
    cpydir("./static","./public")
    generate_page_recursive("./content","template.html","./public")
    #generate_page("./content/index.md","template.html","./public/index.html")
    pass


def generate_page_recursive(dir_path_content,template_path,dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise Exception(f"{dir_path_content} does not exist")
    contents = os.listdir(dir_path_content)

    for item in contents:
        item_full = os.path.join(dir_path_content,item)
        dest_full = os.path.join(dest_dir_path,item).replace(".md",".html")

        if os.path.isfile(item_full):
            generate_page(item_full,template_path,dest_full)
        elif os.path.isdir(item_full):
            generate_page_recursive(item_full,template_path,dest_full)


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for b in blocks:
        if b.startswith("# "):
            return b[2:]

    raise Exception("No title found")
def generate_page(from_path,template_path,dest_path):
    print(f"Generate a page from {from_path} to {dest_path} using {template_path}") 
    
    template = ""
    markdown = ""
    with open(from_path,"r") as f:
        markdown = f.read()
    with open(template_path,"r") as f:
        template = f.read()
    html = markdown_to_html(markdown)
    title = extract_title(markdown)
    template = template.replace("{{ Title }}",title)
    template = template.replace("{{ Content }}",html.to_html())
    dest_dir = os.path.dirname(dest_path)
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path,"w") as f:
        f.write(template)

def cpydir(from_dir,to_dir):
    if os.path.exists(to_dir) and os.path.isdir(to_dir):
        shutil.rmtree(to_dir,onexc=None)
    cpydir_recurse(from_dir,to_dir)

def cpydir_recurse(from_dir,to_dir):
    if not os.path.exists(from_dir):
        raise Exception(f"Directory '{dir}' does not exist.")
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    
    contents = os.listdir(from_dir)
    for item in contents:
        full_path = os.path.join(from_dir,item).replace("\\","/")
        to_full_path = os.path.join(to_dir,item).replace("\\","/")
        if os.path.isdir(full_path):
            cpydir_recurse(full_path,to_full_path)
        elif os.path.isfile(full_path):
            shutil.copy(full_path,to_full_path)
        
main()
