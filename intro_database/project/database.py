from psycopg2 import pool
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


# NOT IDEAL
class ConnectionPool:
    def __init__(self):
        self.connection_pool = pool.SimpleConnectionPool(
            1,
            3,
            user=os.getenv('USER'),
            password=os.getenv('PASS'),
            database=os.getenv('DATABASE'),
            host="localhost"
        )

    def __enter__(self):
        return self.connection_pool.getconn()

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# def connect():
#     return psycopg2.connect(
#         user=os.getenv('USER'),
#         password=os.getenv('PASS'),
#         database=os.getenv('DATABASE'),
#         host="localhost"
#     )
