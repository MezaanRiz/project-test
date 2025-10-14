from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from utils import users


app = FastAPI()

def on_startup():
    SQLModel.metadata.create_all(engine)   # creates tables on startup

app.add_event_handler("startup", on_startup)

app.include_router(users.router, prefix= "/users", tags=["Users"])
