from markdown_blocks import markdown_to_blocks, block_to_html_node
import re


def extract_title(markdown):
    for line in markdown.split("\n"):
        res = re.search(r"^# (.+)$", line)
        if res:
            return res.group(1)

    raise ValueError("No H1 header found")


res = extract_title("""# Tolkien Fan Club
        
![JRR Tolkien sitting](/images/tolkien.png)

Here's the deal, **I like Tolkien**.

> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
""")
print(res)
