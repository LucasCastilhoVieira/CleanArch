from fastapi import APIRouter
from pydantic import BaseModel
from infrastructure.db.repositories.usuariosRepository import UsersRepository
from app.use_cases.user_register import UserRegister

from fastapi import Depends

class Users(BaseModel):
    nome:str
    cpf:int
    telefone:int
    email:str



router = APIRouter(prefix='/api')
UseRegister = lambda: UserRegister(repository=UsersRepository())

@router.post("/Users") #type: ignore

def register_user(Users: Users, use_case: UserRegister = Depends(UseRegister)):
        insert = use_case.register(Users.nome, Users.cpf, Users.telefone, Users.email)
        return insert

    
    
