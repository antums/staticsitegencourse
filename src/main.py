import os
import shutil
from copystatic import copy_files_recursive
from gencontent import generate_page_recursive

dir_static = "./static"
dir_public = "./public"
dir_content = "./content"
dir_template = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static, dir_public)

    print("Generating page...")
    generate_page_recursive(dir_content, dir_template, dir_public)
if __name__ == "__main__":
    main()