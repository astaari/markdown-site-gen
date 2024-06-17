from markdown import *
import unittest
from textnode import * 


class TestMarkdownSplit(unittest.TestCase):
    def test_eq_delimiter(self):
        expecting = [
                TextNode("bold text","bold"),
                TextNode(" and then some ","text"),
                TextNode("more bold ","bold"),
                TextNode(" for you.","text"),
                TextNode(" then some code",'code')
                ]
        initial_nodes = [
                            TextNode("*bold text* and then some *more bold * for you.","text"),
                            TextNode(" then some code",'code'),
                         ]
        result = split_nodes_delimiter(initial_nodes,'*',"bold")
        self.assertEqual(result,expecting)

    def test_except(self):
        text_unclosed = "*unclosed markdown"
        node_unclosed = TextNode(text_unclosed,"text")
        self.assertRaises(Exception,split_nodes_delimiter,
                          [node_unclosed],'*',"bold")
        node_unclosed.text = "unclosed * markdown * but *different"
        self.assertRaises(Exception,split_nodes_delimiter,
                          [node_unclosed],'*',"bold")

        self.assertRaises(ValueError,split_nodes_delimiter,[],'*','bold')
    def test_eq_link(self):
        expecting = [ 
            TextNode("This is text with a ", type_text),
            TextNode("link", type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", type_text),
            TextNode(
                "second link", type_link, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ] 
        node = TextNode(
            "This is text with a [link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another [second link](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )

        self.assertEqual(split_nodes_link([node]),expecting)

        expecting_multiple = [
                TextNode("Cool link",type_link,url="https://thisisalink.com"),
                TextNode(" is here!",type_text),
                TextNode(" And then we have another ",type_text),
                TextNode("link",type_link,url="https://example.com/link"),
                TextNode("!",type_text),
                ]

        node_m1 = TextNode( "[Cool link](https://thisisalink.com) is here!",type_text)
        node_m2 = TextNode(" And then we have another [link](https://example.com/link)!",type_text)
        split2 = split_nodes_link([node_m1,node_m2])
        self.assertEqual(split2,expecting_multiple)
        
    def test_eq_image(self):
        expecting = [ 
            TextNode("This is text with an ", type_text),
            TextNode("image", type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            TextNode(" and another ", type_text),
            TextNode(
                "second image", type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
            ),
        ] 
        node = TextNode(
            "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
            "text",
        )
        

        self.assertEqual(split_nodes_image([node]),expecting)

        expecting_multiple = [
                TextNode("Cool image",type_image,url="https://thisisawebsite.com/image.png"),
                TextNode(" is here!",type_text),
                TextNode(" And then we have another ",type_text),
                TextNode("image",type_image,url="https://example.com/link.png"),
                TextNode("!",type_text),
                ]

        node_m1 = TextNode( "![Cool image](https://thisisawebsite.com/image.png) is here!",type_text)
        node_m2 = TextNode(" And then we have another ![image](https://example.com/link.png)!",type_text)
        split2 = split_nodes_image([node_m1,node_m2])
        self.assertEqual(split2,expecting_multiple)


        


class TestMarkdownImage(unittest.TestCase):
    def test_eq(self):
        text1 = "an ![image](to/my/img)"
        res1 = extract_markdown_images(text1)
        self.assertEqual(res1,[('image','to/my/img')])
        
        text_link_syntax = "not [an image](https://example.com)"
        res_link_syntax = extract_markdown_images(text_link_syntax)
        self.assertEqual([],res_link_syntax)
    

class TestMarkdownLink(unittest.TestCase):
    def test_eq(self):
        text_valid = "Oh boy, a [link !](https://example.com)"
        res1 = extract_markdown_links(text_valid)
        self.assertEqual([('link !','https://example.com')],res1)

        text_img_syntax = "not ![a ... link#%](src/img.jpg)"
        res_img_syntax = extract_markdown_links(text_img_syntax)
        self.assertEqual([],res_img_syntax)

