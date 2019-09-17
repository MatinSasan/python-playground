import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


class User:
    def __init__(self, email, first_name, last_name, id):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        return f"User {self.email}"

    def save_to_db(self):
        with psycopg2.connect(
            user=os.getenv('USER'),
            password=os.getenv('PASS'),
            database=os.getenv('DATABASE'),
            host="localhost"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO users (email, first_name, last_name)' +
                    ' VALUES (%s, %s, %s)',
                    (self.email, self.first_name, self.last_name))
