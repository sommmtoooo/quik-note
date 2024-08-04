from quik_note.db import get_database_connection
from quik_note.model import User
from quik_note.utils import generate_unique_id
from mysql.connector.errors import DatabaseError, IntegrityError

class UserDAO:

    def create_user(self, username: str, password: str):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "INSERT INTO users (id, username, password) VALUES (%s, %s, %s)"
        values = (generate_unique_id(), username, password)
        try:
            cursor.execute(sql, values)
            self.connection.commit()
            return ('Account Created', 'success', True)
        except IntegrityError:
            return ('Username Taken', 'warning', False)
        except DatabaseError:
            return ('Cannot Run Query Now', 'error', False)
        except Exception as e:
            return ('Something went wrong', 'error', False)
        finally:
            cursor.close()
            self.connection.close()

    def get_user_by_username(self, username: str):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "SELECT * FROM users WHERE username = %s;"
        values = (username,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchmany(size=1)
            return [User(x[0], x[1], x[2]) for x in result][0]
        except Exception as error:
            return None
        finally:
            cursor.close()
            self.connection.close()

    def get_user_by_id(self, id: str):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "SELECT * FROM users WHERE id = %s"
        values = (id,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchmany(size=1)
            return [User(x[0], x[1], x[2]) for x in result][0]
        except Exception:
            return None
        finally:
            cursor.close()
            self.connection.close()

