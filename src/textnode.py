from htmlnode import * 

type_text = "text"
type_link = "link"
type_image = "image"
type_bold = "bold"
type_italic = "italic"
type_code = "code"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text=text
        self.text_type=text_type
        self.url=url
    def __eq__(self,o):
        return (
                self.text==o.text and
                self.text_type==o.text_type and
                self.url==o.url
                )
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
def text_node_to_html_node(text_node : TextNode) -> HTMLNode:
    if text_node.text_type==type_text:
        return LeafNode(None,text_node.text) 
    if text_node.text_type==type_bold:
        return LeafNode("b",text_node.text) 
    if text_node.text_type==type_italic:
        return LeafNode("i",text_node.text) 

    if text_node.text_type==type_code:
        return LeafNode("code",text_node.text) 
    if text_node.text_type==type_link:
        return LeafNode("a", text_node.text, props={'href':text_node.url}) 
    if text_node.text_type==type_image:
        return LeafNode("img", "",props={
            'src': text_node.url if text_node.url is not None else "",
            'alt': text_node.text if text_node.text is not None else "",
            })

    raise TypeError(f"Text node of type {text_node.text_type} can't be converted \
            to html")

