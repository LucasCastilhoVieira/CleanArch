from app.use_cases.user_finder import UserFinderUseCase
from infrastructure.db.repositories.usuariosRepository import UsersRepository
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Depends



router = APIRouter(prefix='/FindUser')

UseCase = lambda: UserFinderUseCase(repository=UsersRepository())

@router.get('/Encontrar_usuario')
def get_info(cpf: int, usecase: UserFinderUseCase = Depends(UseCase)):

    select = usecase.find(cpf)    
    return select
    
    
    
