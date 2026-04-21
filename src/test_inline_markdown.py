import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("hello 'world' test", TextType.TEXT)
        result = split_nodes_delimiter([node], "'", TextType.CODE)
        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.CODE),
            TextNode(" test", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_delim_bold(self):
        node = TextNode("hello **world** test", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" test", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_delim_bold_double(self):
        node = TextNode("hello **world** and **world** test", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("hello ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("world", TextType.BOLD),
            TextNode(" test", TextType.TEXT),
        ]
        self.assertEqual(result, expected)
    

if __name__ == "__main__":
    unittest.main()
