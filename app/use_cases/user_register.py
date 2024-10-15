from app.interfaces.use_case_interfaces.users_register import UserRegister as UserRegisterInterface
from app.interfaces.users_repository import UsersRepositoryInterface
from typing import Dict

class UserRegister(UserRegisterInterface):
    def __init__(self, repository: UsersRepositoryInterface):
        self.repository = repository
        
    
    def register(self, nome: str, cpf: int, telefone: int, email: str) -> Dict:  #type: ignore
        self.verification_name(nome)
        self.repository.insert(nome, cpf, telefone, email)
        response = self.__format_response(nome, cpf, email)
        
        return response
    
    @classmethod
    def verification_name(cls, name):
        if len(name) > 30:
            raise Exception('NOME MUITO GRANDE')
    
    @classmethod
    def __format_response(cls, nome, cpf, email):
        
        
        response = {
            "type": "Users",
            "Count": 1,
            "Attributes": {
                "nome": nome,
                "cpf": cpf,
                "email": email
            }
        }
        
        return response
        
        
        