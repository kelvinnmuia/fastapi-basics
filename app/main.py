from typing import Optional, List

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# from passlib.context import CryptContext
import time
from sqlalchemy.orm import Session
from fastapi import Depends
# from . import models, schemas, utils
# from .database import engine, get_db
from app.routers import auth, post, user


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()


my_posts = [{"title": "title of post 1", "content": "content of post 1", "published": True, "rating": 5, "id": 1}, 
            {"title": "favorite foods", "content": "I like pizza", "published": False, "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcom to my first api"}