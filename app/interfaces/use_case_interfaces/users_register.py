from abc import ABC, abstractmethod
from typing import Dict

class UserRegister(ABC):

    @abstractmethod
    def register(cls, nome: str, cpf: int, telefone: int, email: str) -> Dict: pass
    
