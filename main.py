from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .database import  engine
import models 
 
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/show-message")
async def welcome_diasplay():

    return {"data":{ "message": "Hello World"}}

@app.post("/add-user")
def add_user(name: str, email: str):
    return 


@app.get("/what")
def index():
    return JSONResponse (content={"message": "Welcome to the API!"})