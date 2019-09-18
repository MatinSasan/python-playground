from psycopg2 import pool
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    connection_pool = None

    @classmethod
    def initialize(cls):
        Database.connection_pool = pool.SimpleConnectionPool(
            1,
            3,
            user=os.getenv('USER'),
            password=os.getenv('PASS'),
            database=os.getenv('DATABASE'),
            host="localhost"
        )

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.connection_pool.closeall()


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)


# def connect():
#     return psycopg2.connect(
#         user=os.getenv('USER'),
#         password=os.getenv('PASS'),
#         database=os.getenv('DATABASE'),
#         host="localhost"
#     )
