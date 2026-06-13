import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "test", "child")
        node2 = HTMLNode("p", "test", "child")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("p", "test", "child")
        node2 = HTMLNode("h1", "test", "child")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("p", "test", "child", {"key": "value"})
        self.assertEqual("p, test, child, key=\"value\"", repr(node))


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "this is a link", {
                        "href": "https://www.boots.dev"})
        self.assertEqual(
            node.to_html(), "<a href=\"https://www.boots.dev\">this is a link</a>")

    def test_repr(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual("p, Hello, World!, ", repr(node))


if __name__ == "__main__":
    unittest.main()
