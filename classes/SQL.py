import pymysql


class SQL:
    def __init__(self, username, password, database, host):
        self.username = username
        self.password = password
        self.db = database
        self.host = host
        self.connection = pymysql.connect(host=self.host,
                                          user=self.username,
                                          password=self.password,
                                          db=self.db, autocommit=True
)

        self.cursor = self.connection.cursor()

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor

    def __del__(self):
        self.cursor.close()
        self.connection.close()