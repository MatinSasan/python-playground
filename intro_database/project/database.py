from psycopg2 import pool
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

connection_pool = pool.SimpleConnectionPool(
    1,
    3,
    user=os.getenv('USER'),
    password=os.getenv('PASS'),
    database=os.getenv('DATABASE'),
    host="localhost"
)


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)


# def connect():
#     return psycopg2.connect(
#         user=os.getenv('USER'),
#         password=os.getenv('PASS'),
#         database=os.getenv('DATABASE'),
#         host="localhost"
#     )
