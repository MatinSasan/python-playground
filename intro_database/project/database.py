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


# def connect():
#     return psycopg2.connect(
#         user=os.getenv('USER'),
#         password=os.getenv('PASS'),
#         database=os.getenv('DATABASE'),
#         host="localhost"
#     )
