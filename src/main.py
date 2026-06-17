import os
import sys
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

dir_path_content = "./content"
template_path = "./template.html"


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: basepath argument required")
        exit(1)

    basepath = sys.argv[1]
    print("basepath:", basepath)

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating page...")

    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_docs,
        basepath
    )


main()
