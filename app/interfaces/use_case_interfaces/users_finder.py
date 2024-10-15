from abc import ABC, abstractmethod


class UserFinder(ABC):  
    
    @abstractmethod
    def find(cls, cpf): pass