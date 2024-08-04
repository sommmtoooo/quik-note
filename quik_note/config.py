from os import urandom, getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = urandom(24)
    DB_NAME = getenv('DB_NAME') 
    DB_USERNAME = getenv('DB_USERNAME')
    DB_PASSWORD = getenv('DB_PASSWORD')
    DB_HOST = getenv('DB_HOST') 
