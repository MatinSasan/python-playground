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


class ConnectionFromPool:
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        connection_pool.putconn(self.connection)


# def connect():
#     return psycopg2.connect(
#         user=os.getenv('USER'),
#         password=os.getenv('PASS'),
#         database=os.getenv('DATABASE'),
#         host="localhost"
#     )
