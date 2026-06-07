from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
                            password='P0stgres@26', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)

    

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


@app.get("/")
async def root():
    return {"message": "Welcom to my first api"}

@app.get("/posts")
# async def get_posts():
#    return {"data": my_posts}
async def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}

# @app.post("/createpost")
# def create_post(payload: dict = Body(...)):
#    print(payload)
#    return {"newpost": f"title: {payload['title']} content: {payload['content']}"}

# title str, content str, category str, published bool

@app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(post: Post):
    # print(post.dict())
#    post_dict = post.dict()
#    post_dict["id"] = randrange(0, 1000000)
#    my_posts.append(post_dict)
#    return {"data": post_dict}
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
                    (post.title, post.content, post.published))
    new_post = cursor.fetchone()

    conn.commit()

    return {"data": new_post}

# @app.get("/posts/latest")
# def get_latest_post():
#    post = my_posts[len(my_posts) - 1]
#    return {"latest_post": post}

@app.get("/posts/{id}")
# def get_post(id: int, response: Response):
# def get_post(id: int):
#    post = find_post(id)
#    if not post:
#            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#                                detail=f"post with id: {id} was not found")
        # response.status_code = 404
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with id: {id} was not found"}
#    return {"post_detail": post}

def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id),))
    post = cursor.fetchone()
    if not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find the index in the array that has required id
    # my_posts.pop(index)
    # index = find_index_post(id)

    # if index == None:
    #   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
    #                        detail=f"post with id: {id} was not found")
    # my_posts.pop(index)
    # return {"message": f"post with id: {id} was successfully deleted"}
    # return Response(status_code=status.HTTP_204_NO_CONTENT)
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    print(post)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} was not found")
    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict
    return {"data": post_dict}