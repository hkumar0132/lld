from abc import ABC, abstractmethod
from typing import List

class IStudentBuilder(ABC):
    @abstractmethod
    def set_roll_no(self):
        pass

    @abstractmethod
    def set_name(self):
        return self
    
    @abstractmethod
    def set_age(self):
        return self
    
    @abstractmethod
    def set_standard(self):
        return self
    
    @abstractmethod
    def set_subjects(self):
        pass

    @abstractmethod
    def build(self):
        pass