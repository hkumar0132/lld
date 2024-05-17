from IFileSystem import IFileSystem

class File(IFileSystem):

    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def ls(self):
        print(self.file_name)