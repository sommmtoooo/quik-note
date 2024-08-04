import mysql.connector as database

from quik_note.config import Config;

def get_database_connection():
    return database.connect(
    host=Config.DB_HOST,
    username=Config.DB_USERNAME,
    password=Config.DB_PASSWORD,
    database=Config.DB_NAME
)

connection = get_database_connection()
cursor = connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(50) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(250) NOT NULL
);


CREATE TABLE IF NOT EXISTS notes (
    id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    title VARCHAR(250) NOT NULL,
    content TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);
""")

cursor.close()
connection.close()
