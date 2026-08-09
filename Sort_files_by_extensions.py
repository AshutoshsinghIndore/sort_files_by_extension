import os
import shutil
from pathlib import Path


class SortFiles:

    def __init__(self):
        self.path = Path(input("Enter Path: "))

    def list_files(self, path):
        file_list = []

        for root, dirs, files in os.walk(path):
            for file in files:
                file_list.append(Path(root) / file)

        print(f"{len(file_list)} files found..!!")
        return file_list

    def sort_file(self, src_path):
        file_name = src_path.name
        ext = src_path.suffix

        # Handle files without an extension
        folder_name = ext[1:] if ext else "no_extension"

        dst_dir = self.path / "sorted_files" / folder_name
        dst_dir.mkdir(parents=True, exist_ok=True)

        dst_path = dst_dir / file_name

        shutil.move(src_path, dst_path)

    def __call__(self):
        file_list = self.list_files(self.path)

        for file in file_list:
            self.sort_file(file)


if __name__ == "__main__":
    sorter = SortFiles()
    sorter()
