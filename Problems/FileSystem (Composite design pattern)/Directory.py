from typing import List

from IFileSystem import IFileSystem

class Directory(IFileSystem):

    def __init__(self, directory_name: str, child: List[IFileSystem] = []) -> None:
        self.directory_name = directory_name
        self.child : List[IFileSystem] = child

    def add_file_or_directory(self, c: IFileSystem):
        self.child.append(c)

    def ls(self):
        print(f"{self.directory_name}/")
        for c in self.child:
            c.ls()