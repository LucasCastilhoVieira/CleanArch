
from app.interfaces.users_repository import UsersRepositoryInterface
from infrastructure.db.settings.connection import ConnectionDBHandler
from infrastructure.db.entities.usuarios import UsuariosEntities
from app.interfaces.models.Users import Users
from typing import List

class UsersRepository(UsersRepositoryInterface):

    
    def insert(self, nome:str, cpf:int, telefone:int, email:str):

        with ConnectionDBHandler() as connection:
            insert = UsuariosEntities(nome=nome, cpf=cpf, telefone=telefone, email=email) 
            connection.session.add(insert)
            connection.session.commit()
            
    
    def remove_users(self, cpf):
        with ConnectionDBHandler() as Connection:
            Connection.session.query(UsuariosEntities).filter(UsuariosEntities.cpf == cpf).delete()

   
    def select(self, cpf) -> List[Users]:
        with ConnectionDBHandler() as Connection:
            select = Connection.session.query(UsuariosEntities)\
                .with_entities(
                    UsuariosEntities.nome, 
                    UsuariosEntities.cpf, 
                    UsuariosEntities.email,
                    UsuariosEntities.telefone)\
                .filter(UsuariosEntities.cpf == cpf).all()
            return select
        