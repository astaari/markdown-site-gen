from htmlnode import *
from markdown import text_to_text_node
from textnode import text_node_to_html_node
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

block_html_dict = {
            block_type_paragraph:'p',
            block_type_heading:'h#',
            block_type_code:'pre',
            block_type_quote:'blockquote',
            block_type_unordered_list:'ul',
            block_type_ordered_list:'ol'
        }

list_element = 'li'
code_element = 'code'


def markdown_to_blocks(markdown):
    block_strings = markdown.split("\n\n")
    result = []
    for s in block_strings:
        if not s:
            continue
        result.append(s.strip())
    return result 


def block_to_block_type(block):
    import re
    lines = block.split("\n")


    if re.match("^[(#)]{1,6}",block):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith("* ") or block.startswith("- "):
        for line in lines:
            if not line.startswith("* ") and not line.startswith("- "):

                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("1."):
        itr = 2
        for line in lines[1:]:
            if not line.startswith(f"{itr}."):
                return block_type_paragraph
            itr+=1
        return block_type_ordered_list
    return block_type_paragraph
def get_header_html(block):
    lines = block.split("\n")
    elements = []
    for l in lines:
        pounds = l.split(" ",1)
        count = len(pounds[0])
        if count > 6 or count < 1:
            raise ValueError(f"Header markdown contained more than 6 or less that 1 '#'\n\tline:{l}")
        sub_children = []
        txt_nodes = text_to_text_node(pounds[1])
        for n in txt_nodes:
            sub_children.append(text_node_to_html_node(n))
        elements.append(ParentNode(f"h{count}",children=sub_children))
    return elements
def get_list_html(block,ordered):
    lines = block.split("\n")
    elements = []
    for l in lines:
        element = l.split(" ",1)[1]
        sub_children = []
        txt_nodes = text_to_text_node(element)
        for n in txt_nodes:
            sub_children.append(text_node_to_html_node(n))
        elements.append(ParentNode("li",children=sub_children))
    parent = ParentNode('ol' if ordered else 'ul',children=elements)
    return parent
def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for b in blocks:
        block_type = block_to_block_type(b)
        tag = block_html_dict[block_type]
        if block_type==block_type_paragraph:

            txt_nodes = text_to_text_node(b)
            sub_children = []
            for n in txt_nodes:
                sub_children.append(text_node_to_html_node(n))

            node =ParentNode(tag,children=sub_children)
            children.append(node)
        elif block_type==block_type_heading:
            for child in get_header_html(b):
                children.append(child) 
        elif block_type==block_type_code:
            #Leave because it's already formatted
            child = LeafNode(code_element,b.strip('```'))
            parent = ParentNode(tag,children=[child])
            children.append(parent)
        elif block_type == block_type_quote:
            text = b.replace('\n>','\n')[2:]
            txt_nodes = text_to_text_node(text)
            sub_children = []
            for n in txt_nodes:
               sub_children.append(text_node_to_html_node(n)) 
            child = ParentNode(tag,children=sub_children)
            children.append(child)
        elif block_type == block_type_unordered_list:
            children.append(get_list_html(b,False))
        elif block_type == block_type_ordered_list:
            children.append(get_list_html(b,True))
    root = ParentNode('div',children=children)

    return root

     
    
