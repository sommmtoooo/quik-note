from mysql.connector.errors import DatabaseError
from quik_note.model import Note
from quik_note.db import get_database_connection

class NoteDAO:

    def create_note(self, note: Note):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "INSERT INTO notes (id, user_id, title, content) VALUES (%s, %s, %s, %s)"
        values = (note.id, note.user_id, note.title, note.content)
        try:
            cursor.execute(sql, values)
            self.connection.commit()
            return ('Note Created', 'success', True)
        except DatabaseError as error:
            return ('Cannot Run Query Now', 'error', False)
        except Exception as e:
            return ('Something went wrong', 'error', False)
        finally:
            cursor.close()
            self.connection.close()

    def update_note(self, note: Note):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "UPDATE notes SET title=%s, content=%s WHERE id = %s"
        values = (note.title, note.content, note.id)
        try:
            cursor.execute(sql, values)
            self.connection.commit()
            return ('Note Updated', 'success', True)
        except DatabaseError as error:
            return ('Cannot Run Query Now', 'error', False)
        except Exception as e:
            return ('Something went wrong', 'error', False)
        finally:
            cursor.close()
            self.connection.close()

    def delete_note(self, id: str):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "DELETE FROM notes WHERE id = %s"
        values = (id,)
        try:
            cursor.execute(sql, values)
            self.connection.commit()
            return ('Note Deleted', 'success', True)
        except DatabaseError as error:
            return ('Cannot Run Query Now', 'error', False)
        except Exception as e:
            return ('Something went wrong', 'error', False)
        finally:
            cursor.close()
            self.connection.close()

    def get_user_note(self, user_id: str):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "SELECT * FROM notes WHERE user_id = %s"
        values = (user_id,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchall()
            return [Note(x[0], x[1], x[2], x[3]) for x in result]
        except Exception as e:
            return None
        finally:
            cursor.close()
            self.connection.close()

    def get_note(self, id: str):
        self.connection = get_database_connection()
        cursor = self.connection.cursor()
        sql = "SELECT * FROM notes WHERE id = %s"
        values = (id,)
        try:
            cursor.execute(sql, values)
            result = cursor.fetchmany(size=1)
            return [Note(x[0], x[1], x[2], x[3]) for x in result][0]
        except Exception as e:
            return None
        finally:
            cursor.close()
            self.connection.close()

