import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


def connect():
    return psycopg2.connect(
        user=os.getenv('USER'),
        password=os.getenv('PASS'),
        database=os.getenv('DATABASE'),
        host="localhost"
    )
