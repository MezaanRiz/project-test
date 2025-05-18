from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id : int  = Column( primary_key=True, index=True)
    name : str = Column( index=True, nullable=False)
    email : str = Column ( unique=True, index=True, nullable=False)

    items = relationship("Item", back_populates="owner")