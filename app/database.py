from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

#print(settings.database_hostname)
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
#print("CHECK OUT HERE",SQLALCHEMY_DATABASE_URL)
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='andrewicho', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()

#         print("Database connection was successful!")
#         break
#         # data1 = cursor.execute('SELECT * FROM posts;')
#         # print(data1)
#     except Exception as error:
#         print("Connecting to database failed")
#         print("error was:", Exception)
#         time.sleep(2)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
