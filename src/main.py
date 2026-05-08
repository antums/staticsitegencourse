import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_page_recursive


dir_static = "./static"
dir_public = "./docs"
dir_content = "./content"
dir_template = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    print("Deleting public directory...")
    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static, dir_public)

    print("Generating page...")
    generate_page_recursive(dir_content, dir_template, dir_public, basepath)
if __name__ == "__main__":
    main()