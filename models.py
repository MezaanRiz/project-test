from sqlmodel import SQLModel, Field, Session, Column, Integer, String, ForeignKey, Relationship
from typing import List, Optional
from sqlmodel import Session
from enum import Enum



class UserBase(SQLModel):

    email: str = Field(sa_column=Column(String, unique=True, index=True))
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)

    
    
class User(UserBase, table=True):
    __tablename__ = "users"
    id: Optional[int] = Field(default=None, primary_key=True)

 
class UserCreate(UserBase):
    pass

class UserRead(User):
    id: int

