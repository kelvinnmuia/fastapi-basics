from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"message": "Welcom to my first api"}

@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}

# @app.post("/createpost")
# def create_post(payload: dict = Body(...)):
#    print(payload)
#    return {"newpost": f"title: {payload['title']} content: {payload['content']}"}

# title str, content str, category str, published bool

@app.post("/createpost")
def create_post(new_post: Post):
    print(new_post.dict())
    return {"data": new_post}