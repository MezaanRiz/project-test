from sqlmodel import  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = 'sqlite:///database.db'


Sqlsession =  sessionmaker(auto_commit=False, autoflush=False, bind=engine)

Base = declarative_base()

