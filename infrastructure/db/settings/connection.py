from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
class ConnectionDBHandler:
    def __init__(self):
        self.engine = 'mysql+pymysql://root:lucas@172.18.0.10/cadastrousuarios'
        self.session = None
        self.__engine = self.get_engine()
    
    
    def get_engine(self):
        engine = create_engine(self.engine)
        return engine
    
    
    def engine(self):
        return self.__engine
    
    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self
    
    
    def __exit__(self, exc_val, exc_tb, exc_type):
        return self.session.close()
        
    