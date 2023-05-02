from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
from . import utils
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from .routers import post, user

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi',
                                user='andrewicho', cursor_factory=RealDictCursor)
        cursor = conn.cursor()

        print("Database connection was successful!")
        break
        # data1 = cursor.execute('SELECT * FROM posts;')
        # print(data1)
    except Exception as error:
        print("Connecting to database failed")
        print("error was:", Exception)
        time.sleep(2)

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

app.include_router(post.router)
app.include_router(user.router)
@app.get("/")
def root():
    return {"data": "test data"}

