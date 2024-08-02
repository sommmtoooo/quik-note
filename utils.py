from db import get_database_connection
from mysql.connector.errors import DatabaseError, IntegrityError
from uuid import uuid4



def create_user(username: str, password: str):
    connection =get_database_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
    unique_id = uuid4()
    values = (str(unique_id), username, password)
    try:
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        return ('Account Created', 'success', True)
    except IntegrityError:
        return ('Username Taken', 'warning', False)
    except DatabaseError:
        return ('Cannot Run Query Now','error', False)
    except:
        return ('Something went wrong', 'error', False)
    

def get_user_by_username(username: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE username = %s;"
    values = (username,)
    cursor.execute(sql,values)
    try:
        result = cursor.fetchmany(size=1)
        print(result)
        connection.close()
        return [{'id': x[0], 'username': x[1], 'password': x[2] } for x in result][0]
    except Exception as error:
        return None

def get_user_by_id(id: str):
    connection = get_database_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE id = %s"
    values = (id,)
    try:
        cursor.execute(sql,values)
        result = cursor.fetchmany(size=1)
        connection.close()
        return [{'id': x[0], 'username': x[1], 'password': x[2] } for x in result][0]
    except Exception:
        return None
