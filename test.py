from app.use_cases.user_register import UserRegister
from infrastructure.db.repositories.usuariosRepository import UsersRepository

users = UserRegister(UsersRepository) #type: ignore

insert = users.register('lucas', 2974293, 234543534,'kaschoasdo')
print(insert)