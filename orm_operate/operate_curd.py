from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text
engine = create_engine("mysql+mysqlconnector://root:111@10.:3/test", encoding='utf-8')


Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    userName = Column(String)
    password = Column(String)
    age = Column(String)
    sex = Column(String)
    isDelete = Column(String)
    permission = Column(String)








