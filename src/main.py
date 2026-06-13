from textnode import TextNode, TextType


def main():
    print("Hello World")
    text_node = TextNode("This is some anchor text",
                         TextType.PLAIN, "https://www.boot.dev")
    print(text_node)


main()
