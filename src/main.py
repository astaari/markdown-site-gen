from textnode import *
from htmlnode import *
from markdown import *
def main():
    node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    "text",
    )
    new_nodes = split_nodes_image([node])
    print("[")
    for n in new_nodes:
        print(n)
    print("]")

    node2 = TextNode(
    "[an image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    "text",
    )
    
    node_m1 = TextNode( "[Cool link](https://thisisalink.com) is here!",type_text)
    print("4$##%#$")
    new_nodes = split_nodes_link([node_m1,node2])
    print("003000222")
    print("[")
    for n in new_nodes:
        print(n)
    print("]")
#    node=TextNode("This is a link","link",url="https://www.google.com")
#    node2 = TextNode("This is an image","image",url="link/to/my/image.png")
#    node3 = TextNode("some bold text","bold")
#    node4 = TextNode(None,"image")
#    print(text_node_to_html_node(node).to_html())
#    print(text_node_to_html_node(node2).to_html())
#    print(text_node_to_html_node(node3).to_html())
#    print(text_node_to_html_node(node4).to_html())
    


main()
