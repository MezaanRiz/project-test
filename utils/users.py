from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from database import get_session
from models import User, UserCreate, UserRead

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user_in: UserCreate, session: Session = Depends(get_session)):
   
    existing = session.exec(select(User).where(User.email == user_in.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    orm_user = User.model_validate(user_in)
    session.add(orm_user)
    session.commit()
    session.refresh(orm_user)
    return orm_user

@router.get("/users/{user_id}", response_model=UserRead)
def read_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/users/", response_model=List[User])
def list_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    statement = select(User).offset(skip).limit(limit)
    users = session.exec(statement).all()
    return users