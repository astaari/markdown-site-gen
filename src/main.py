from block_markdown import block_to_block_type, get_header_html, markdown_to_html
from textnode import *
from htmlnode import *
from markdown import *
from block_markdown import *

import os
import sys
import shutil
def main():
    print(sys.argv[1:])
    from_dir,to_dir=sys.argv[1:]
    #from_dir,to_dir = sys.argv[1]
    cpydir(from_dir,to_dir)
    pass

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
            cpy_directory(full_path,to_full_path)
        elif os.path.isfile(full_path):
            shutil.copy(full_path,to_full_path)
        
main()
