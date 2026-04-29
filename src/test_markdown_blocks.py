import unittest
from markdown_blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestMarkdownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraph(self):
        block = "this is a normal paragraph"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading(self):
        block = "# Hello"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_code_block(self):
        block = "```\nprint('hi')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_quote_block(self):
        block = "> first line\n> second line"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_unordered_list(self):
        block = "- one\n- two\n- three"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. one\n2. two\n3. three"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)