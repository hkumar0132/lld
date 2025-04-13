'''
# API - Search the File System
# Searching Files based on Name, Extension and Size

# Input for the search (directory)
# 1. Does this support both file and directory?
# 2. Operations allowed -> create, read, delete on files/directory?
# 3. Search filters
# 4. Is same file name allowed in same level?
# 5. Any constraints on file size

# Functional requirements:
# 1. Create, read, delete a file/directory
# 2. Search by name, extension size but extensible

# Core entities:
# 1. File
# 2. Directory
# 3. FileSystem
#        []
#        /\
#      /  \ \
#     ()   [] ()
#            []

# 4. Filter
# 5. NameFilter
# 6. SizeFilter
# 7. ExtensionFilter
# 8. Search

Design patterns
1. Strategy design pattern for filters
2. Composite design pattern for Directory and File

'''

# Python implementation

# exceptions.py
class DuplicateFileNameException(Exception):
    def __init__(self, message='This file already exists'):
        super().__init__(message)


# enums.py
from enum import Enum

class FileExtension(Enum):
    JPG = 'JPG'
    JPEG = 'JPEG'
    PDF = 'PDF'
    MKV = 'MKV'


# file_system_entities.py
from enums import FileExtension
from exceptions import DuplicateFileNameException

class File:
    def __init__(self, name: str, size: int, extension: FileExtension):
        self.name = name
        self.size = size
        self.extension = extension

    def __repr__(self):
        return f"File(name={self.name}, size={self.size}, extension={self.extension.name})"


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.files = []
        self.directories = []

    def add_file(self, new_file: File):
        if any(f.name == new_file.name for f in self.files):
            raise DuplicateFileNameException()
        self.files.append(new_file)

    def remove_file(self, file_name: str):
        self.files = [f for f in self.files if f.name != file_name]

    def add_directory(self, directory):
        self.directories.append(directory)

    def get_files(self):
        return self.files

    def get_directories(self):
        return self.directories


class FileSystem:
    def __init__(self, root: Directory):
        self.root = root

    def get_root(self):
        return self.root


# filters.py
from abc import ABC, abstractmethod

class Filter(ABC):
    @abstractmethod
    def match(self, file):
        pass


class NameFilter(Filter):
    def __init__(self, target_name: str):
        self.target_name = target_name

    def match(self, file):
        return file.name == self.target_name


class ExtensionFilter(Filter):
    def __init__(self, extensions):
        self.extensions = extensions

    def match(self, file):
        return file.extension in self.extensions


class SizeFilter(Filter):
    def __init__(self, size: int, operator: str):
        self.size = size
        self.operator = operator

    def match(self, file):
        if self.operator == '>':
            return file.size > self.size
        elif self.operator == '<':
            return file.size < self.size
        elif self.operator == '=':
            return file.size == self.size
        elif self.operator == '>=':
            return file.size >= self.size
        elif self.operator == '<=':
            return file.size <= self.size
        else:
            raise ValueError('Invalid operator')


# search.py
class Search:
    def __init__(self, file_system, filters, logic='AND'):
        self.root = file_system.get_root()
        self.filters = filters
        self.logic = logic

    def _matches(self, file):
        results = [f.match(file) for f in self.filters]
        if self.logic == 'AND':
            return all(results)
        elif self.logic == 'OR':
            return any(results)
        else:
            raise ValueError('Invalid logic operator')

    def _traverse(self, file_system, results):
        if isinstance(file_system, File):
            if self._matches(file):
                results.append(file)
            return
          
        for file in directory.get_files():
            self._traverse(file, results)

        for sub_dir in directory.get_directories():
            self._traverse(sub_dir, results)

    def search(self):
        result = []
        self._traverse(self.root, result)
        return result


# main.py
from file_system_entities import File, Directory, FileSystem
from enums import FileExtension
from filters import NameFilter, ExtensionFilter, SizeFilter
from search import Search

if __name__ == "__main__":
    f1 = File("a1", 10, FileExtension.JPG)
    f2 = File("a2", 20, FileExtension.JPEG)
    f3 = File("a3", 30, FileExtension.MKV)
    f4 = File("a4", 40, FileExtension.PDF)

    root_dir = Directory("root")
    root_dir.add_file(f1)
    root_dir.add_file(f2)

    sub_dir = Directory("sub")
    sub_dir.add_file(f3)
    sub_dir.add_file(f4)

    root_dir.add_directory(sub_dir)

    fs = FileSystem(root_dir)

    filters = [
        NameFilter("a1"),
        SizeFilter(15, '>'),
        ExtensionFilter([FileExtension.JPG, FileExtension.MKV])
    ]

    search = Search(fs, filters, logic='OR')
    result = search.search()

    print("Matched Files:", result)
