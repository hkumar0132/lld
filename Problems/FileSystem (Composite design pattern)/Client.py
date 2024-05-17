from File import File
from Directory import Directory

class Client:

    '''
    
        directory2\
            file1
            file2
            directory1
                file3

    
    '''

    file1 = File("file1")
    file2 = File("file2")
    file3 = File("file3")

    directory1 = Directory("directory1")
    directory1.add_file_or_directory(file3)
    directory2 = Directory("directory2", [file1, file2])
    directory2.add_file_or_directory(directory1)

    directory2.ls()