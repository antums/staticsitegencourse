import unittest

from textnode import TextNode, TextType
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes
    )

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
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "Test text [link](https://test.com) and [bonus link](https://test2.com) bonus text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Test text ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://test.com"),
                TextNode(" and ", TextType.TEXT),
                TextNode("bonus link", TextType.LINK, "https://test2.com"),
                TextNode(" bonus text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_text_to_text_nodes(self):
        node = "Let me _test_ this **cool** system I made [link](https://test.com)"
        new_nodes = text_to_textnodes(node)
        self.assertListEqual(
            [
                TextNode("Let me ", TextType.TEXT),
                TextNode("test", TextType.ITALIC),
                TextNode(" this ", TextType.TEXT),
                TextNode("cool", TextType.BOLD),
                TextNode(" system I made ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://test.com")
            ],
            new_nodes,
        )
        
if __name__ == "__main__":
    unittest.main()
