import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(props={"href":"https://google.com","target":"_blank"})
        self.assertEqual(node1.props_to_html()," href=\"https://google.com\" target=\"_blank\"")
        node2 = HTMLNode()
        self.assertEqual(node2.props_to_html(),"")

        if __name__ == "__main__":
            unittest.main()
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p","A paragraph!")
        self.assertEqual(node.to_html(),"<p>A paragraph!</p>")
        node2 = LeafNode("a","link to google",props={'href':'https://www.google.com'})
        print(node2.to_html())
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">link to google</a>")

from htmlnode import ParentNode
class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
                         node.to_html())
    def test_with_props(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("a","a link", props={'href':'example.com'}),
                    LeafNode("p","Another paragraph"),
                ],
                )
        self.assertEqual(node.to_html(),"<p><a href=\"example.com\">a link</a><p>Another paragraph</p></p>")
    def test_val_error(self):
        node = ParentNode(None,
                          [LeafNode("p","Paragraph"),]
                          )
        self.assertRaises(ValueError,node.to_html)
