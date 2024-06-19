import re
from textnode import (
        TextNode,
        type_text,
        type_link,
        type_bold,
        type_code,
        type_image,
        type_italic
        )

delimiter_bold = "**"
delimiter_italic = "*"
delimiter_code = "`"

_imre = re.compile(r"!\[(.*?)\]\((.*?)\)")
_linkre = re.compile(r"(?<!!)\[(.*?)\]\((.*?)\)")



def extract_markdown_images(text):
    matches = _imre.findall(text)
    return matches


def extract_markdown_links(text):
    matches = _linkre.findall(text) 
    return matches

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []

    if len(old_nodes)==0:
        raise ValueError("No nodes passed in 'split_nodes_delimiter'")
    for old in old_nodes:
        if old.text_type!=type_text:
            new_nodes.append(old)
            continue
        split = old.text.split(delimiter)
        if len(split)%2 ==0:
            raise Exception(f"unclosed markdown found at {old}")
        for i in range(0,len(split)):
            if split[i]=="":
                continue
            #TODO might need special check for beginning with delimiter, etc
            if i%2==1:
                new_nodes.append(TextNode(text=split[i],text_type=text_type))
            else:
                new_nodes.append(TextNode(text=split[i],text_type=type_text))

        
    return new_nodes 

def split_nodes_image(nodes):
    result = []
    if not nodes:
        raise Exception("No nodes to operate on")
    for node in nodes:
        if not node.text:
            continue
        matches = extract_markdown_images(node.text)
#        print("MATCHES :: ",matches)
        if not matches or node.text_type != type_text:
            result.append(node)
            continue
        current = node.text 
        for m in matches:
            split_text = current.split(f"![{m[0]}]({m[1]})",1)
            if not split_text[0]:
                result.append(TextNode(m[0],text_type=type_image,url=m[1]))
            else:
                result.append(TextNode(split_text[0],text_type=type_text))
                result.append(TextNode(m[0],text_type=type_image,url=m[1]))
            current = split_text[1]
        if current:    
            result.append(TextNode(current,text_type=type_text))

    return result

def split_nodes_link(nodes):
    result = []
    if not nodes:
        raise Exception("No nodes to operate on")
    for node in nodes:
        if not node.text:
            continue
        matches = extract_markdown_links(node.text)
        if not matches or node.text_type != type_text:
            result.append(node)
            continue
        current = node.text 
        for m in matches:
            split_text = current.split(f"[{m[0]}]({m[1]})",1)
            if not split_text[0]:
                result.append(TextNode(m[0],text_type=type_link,url=m[1]))
            else:
                result.append(TextNode(split_text[0],text_type=type_text))
                result.append(TextNode(m[0],text_type=type_link,url=m[1]))
            current = split_text[1]
        if current:    
            result.append(TextNode(current,text_type=type_text))

    return result
def text_to_text_node(text):
    nodes = [TextNode(text,type_text)]
    if delimiter_bold in text:
        nodes =split_nodes_delimiter(nodes,delimiter_bold,type_bold) 
    if delimiter_italic in text:
        nodes = split_nodes_delimiter(nodes,delimiter_italic,type_italic)
    if delimiter_code in text:
        nodes = split_nodes_delimiter(nodes,delimiter_code,type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
