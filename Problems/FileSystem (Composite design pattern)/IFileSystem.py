from abc import ABC, abstractmethod

class IFileSystem(ABC):

    @abstractmethod
    def ls():
        pass