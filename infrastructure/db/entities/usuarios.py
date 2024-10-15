
from sqlalchemy import Column, CHAR, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class UsuariosEntities(base): #type: ignore
    __tablename__ = 'usuarios'
    nome = Column(VARCHAR(50))
    cpf = Column(CHAR(11), primary_key=True)
    telefone = Column(CHAR(11))
    email = Column(VARCHAR(40))