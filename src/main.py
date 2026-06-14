from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode


def main():
    print("Hello World")
    # text_node = TextNode("This is some anchor text",
    #                      TextType.PLAIN, "https://www.boot.dev")
    # print(text_node)

    parent_node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text")
    ])

    print(parent_node.to_html())


main()
