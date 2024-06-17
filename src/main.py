from textnode import *
from htmlnode import *
from markdown import *
def main():
    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)" 
    nodes = text_to_text_node(text)
    print_nodes(nodes)
    pass
def print_nodes(nodes):
    print("[")
    for n in nodes:
        print(f"\t{n}")
    print("]")
main()
