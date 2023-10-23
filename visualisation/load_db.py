import pymysql

"""
class oracle_connection(object):
    def __init__(self, connection_string=conn_str):
        self.connection_string = connection_string
        self.connector = None

    def __enter__(self):
        self.connector = pymysql.connect(self.connection_string)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()
"""

db_config = {'host': 'localhost',
             'port': 3306,
             'user': 'root',
             'password': 'alamakota',
             'database': 'students_db',  # Replace with your database name
            }

class mysql_connection:
    """ mysql database connection """
    def __init__(self, connection_str):
        self.connection_str = connection_str
        self.connector = None
        
    def get_connection(self):
        """Return the database connection object."""
        #assumption that connection str is a dict, not str
        #worth to add str/dict parser
        self.connector = pymysql.connect(**self.connection_str)
        return self.connector

    def __enter__(self):
        return self.get_connection()

    #add errors, for example what if there is no running db ?
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()


"""
    def __enter__(self):
        self.connector = pymysql.connect(self.connection_string)
        return self
"""
