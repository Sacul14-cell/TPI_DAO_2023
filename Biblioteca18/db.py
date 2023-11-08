import sqlite3

class DBConnection:
    _instance = None
    dbconnection = None
    
    def __new__(cls, connection_string):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls.dbconnection = connection_string
        return cls._instance
    
    def execute(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

