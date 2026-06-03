from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcom to my first api"}

@app.get("/posts")
async def get_posts():
    return {"data": "This is your posts"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"newpost": f"title: {payload['title']} content: {payload['content']}"}