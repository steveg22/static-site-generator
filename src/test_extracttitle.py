import unittest
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_heading_one_single(self):
        markdown = "# Heading 1"
        res = extract_title(markdown)
        self.assertEqual(res, "Heading 1")

    def test_heading_one_multi(self):
        markdown = """# Tolkien Fan Club

        ![JRR Tolkien sitting](/images/tolkien.png)

        Here's the deal, **I like Tolkien**.

        > "I am in fact a Hobbit in all but size."
        >
        > -- J.R.R. Tolkien
        """
        res = extract_title(markdown)
        self.assertEqual(res, "Tolkien Fan Club")

    def test_no_h1_header(self):
        with self.assertRaises(ValueError):
            extract_title("Hello\nWorld")
