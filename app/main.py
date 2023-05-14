from fastapi import FastAPI
from . import utils
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# data1 = cursor.execute('SELECT * FROM posts;')
# print(data1)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"data": "test data"}

