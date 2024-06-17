import unittest

from textnode import * 


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node,node2)

class TextTextNodeToHtmlNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode(text="A link",text_type="link", url="https://www.example.com")
        expect1 = "<a href=\"https://www.example.com\">A link</a>"

        node2 = TextNode(text="An image", text_type="image", url="path/to/my/image.png")
        expect2 = "<img src=\"path/to/my/image.png\" alt=\"An image\"></img>"
        
        node3 = TextNode(text=None, text_type="image", url="path/to/my/image.png")
        expect3 = "<img src=\"path/to/my/image.png\" alt=\"\"></img>"

        node4 = TextNode(text=None, text_type="image", url=None)
        expect4 = "<img src=\"\" alt=\"\"></img>"
        self.assertEqual(text_node_to_html_node(node1).to_html(),expect1)

        self.assertEqual(text_node_to_html_node(node2).to_html(),expect2)
        self.assertEqual(text_node_to_html_node(node3).to_html(),expect3)
        self.assertEqual(text_node_to_html_node(node4).to_html(),expect4)
        pass
    def test_error(self):
        txt_node = TextNode("unknown node","superbold")
        self.assertRaises(TypeError,text_node_to_html_node,txt_node)

if __name__ == "__main__":
    unittest.main()
