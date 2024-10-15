from abc import ABC, abstractmethod
from app.interfaces.models.Users import Users
from typing import List

class UsersRepositoryInterface(ABC):
    
    @abstractmethod
    def insert(cls, nome:str, cpf:int, telefone:int, email:str):pass
    
    @abstractmethod
    def remove_users(cls, cpf): pass
    
    @abstractmethod
    def select(cls, cpf) -> List[Users]: pass