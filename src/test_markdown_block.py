from block_markdown import *
import unittest

from block_markdown import block_to_block_type



class TestBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        input_text = """This is a **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        expecting = ["This is a **bolded** paragraph",
                     "This is another paragraph with *italic* text and `code` here\
\nThis is the same paragraph on a new line",
                     "* This is a list\n* with items"]
        result = markdown_to_blocks(input_text)

        self.assertEqual(result,expecting)

    def test_block_to_block_type(self):
        blocks = ["* unordered list block","> Quote block", " normal paragraph block"]
        result = []
        for b in blocks:
            result.append(block_to_block_type(b))
        expecting = [block_type_unordered_list,block_type_quote,block_type_paragraph]
        self.assertEqual(result,expecting)

    def test_header_blocks(self):
        expected = [block_type_heading for i in range(6)]
        blocks = ["# a list",
                  "## another list",
                  "### third list",
                  "#### fourth",
                  "##### fifth",
                  "###### sixth",
                ]
        result = []
        for b in blocks:
            result.append(block_to_block_type(b))
        self.assertEqual(expected,result)

    def test_unordered_blocks(self):
        blocks = [
                "* item 1\n* item2\n* item3\n* item 4",
                "* an item\n- new item\n not an item",
                "not even an item\n * but this one is",
                "* one in the list",
                "* with star\n- with hyphen\n* with star",
                ]
        expected = [block_type_unordered_list,
                    block_type_paragraph,
                    block_type_paragraph,
                    block_type_unordered_list,
                    block_type_unordered_list]

        result = []
        for b in blocks:
            result.append(block_to_block_type(b))
        self.assertEqual(result,expected)
    def test_quote_blocks(self):
        blocks = [
                ">This is a quote\n>about a moat\n>and not a goat",
                ">Another quote\nBut not this bloke",
                "Not even trying to be a quote\nNope nope nope",
                ]
        
        expected = [block_type_quote,
                    block_type_paragraph,
                    block_type_paragraph,
                    ]
        result = []
        for b in blocks:
            result.append(block_to_block_type(b))
        self.assertEqual(result,expected)
    def test_ordered_list(self):
        blocks = [
                "1. item 1\n2.item 2\n3. item 3\n4. item 4",
                "2. doesn't work",
                "1. item 1\n3. doesn't work",
                ]
        expected = [block_type_ordered_list,
                    block_type_paragraph,
                    block_type_paragraph,
                    ]
        result = []
        for b in blocks:
            result.append(block_to_block_type(b))
        self.assertEqual(result,expected)
    def test_code_block(self):
        blocks = [
                "```This is some code for something```",
                "```this is\n code \n for something```",
                "```This does nothing",
                "``` This is \n good\n```",
                ]
        expected = [block_type_code,
                    block_type_code,
                    block_type_paragraph,
                    block_type_code
                    ]
        result = []
        for b in blocks:
            result.append(block_to_block_type(b))
