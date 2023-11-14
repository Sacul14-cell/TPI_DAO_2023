import sqlite3

class DBConnection:
    _instance = None
    dbconnection = None
    
    def __new__(cls, connection_string):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls.dbconnection = connection_string
            cls.conn = sqlite3.connect(cls.dbconnection)

        return cls._instance
    
    def execute(self, query, values=None, opc=0):
        cursor = self.conn.cursor()

        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            if opc == 0:
                result = cursor.fetchall()
                cursor.close()
                return result
            else:
                self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error de SQLite: {e}")
        finally:
            cursor.close()