import os
import shutil

def copy_files_recursive(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    for item in os.listdir(source_dir):
        from_dir = os.path.join(source_dir, item)
        to_dir = os.path.join(dest_dir, item)
        print(f" * {from_dir} -> {to_dir}")
        if os.path.isfile(from_dir):
            shutil.copy(from_dir, to_dir)
        else:
            copy_files_recursive(from_dir, to_dir)

