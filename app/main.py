from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


try:
    conn = psycopg2.connect(host='localhost', database='fastapi',
                            user='andrewicho', cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    print("Database connection was successful!")
    # data1 = cursor.execute('SELECT * FROM posts;')
    # print(data1)
except Exception as error:
    print("Connecting to database failed")
    print("error was:", Exception)
my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1}, {
    "title": "favorite foods", "id": 2}]

# data1 = cursor.execute('SELECT * FROM posts;')
# print(data1)

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.get("/")
def root():

    return {"data": "test data"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    # print(post.dict()) #turns into a standard python dictionary.
    post_dict = post.dict()
    my_posts.append(post_dict)
    return {"data": post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with idL {id} not found"}
    return {"post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    print(id, type(id))
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    print(index)
    del my_posts[index]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    print(post)
    return {"data": post_dict}

    # return {"message": "updated Post"}
