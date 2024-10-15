from app.interfaces.use_case_interfaces.users_finder import UserFinder
from app.interfaces.users_repository import UsersRepositoryInterface

class UserFinderUseCase(UserFinder):
    def __init__(self, repository: UsersRepositoryInterface):
        self.user_repository = repository
        pass
      
    def find(self, cpf):
        select = self.user_repository.select(cpf)
        self.verification_select(select)
        response = self.format_response(select)
        return response
        
        
        
    @classmethod
    def verification_select(cls, select):
        if select == []:
            return 'error'
        
        
    @classmethod    
    def format_response(cls, select): 
        attributtes = []
        for nome, cpf, telefone, email in select:
            attributtes.append({
                "NOME": nome,
                "CPF": cpf,
                "TELEFONE": telefone,
                "EMAIL": email
            })
            
        return attributtes