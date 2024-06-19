from block_markdown import block_to_block_type
from textnode import *
from htmlnode import *
from markdown import *
from block_markdown import *
def main():
    markdown = """This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items"""
    blocks = markdown_to_blocks(markdown) 
    print(blocks)
    print(len(blocks))
    print(markdown)

    for b in blocks:
        print(block_to_block_type(b))
    pass
def print_nodes(nodes):
    print("[")
    for n in nodes:
        print(f"\t{n}")
    print("]")
main()
