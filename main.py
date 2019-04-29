import pymysql

import pymysql

from classes.password_file import PasswordFile

conn = pymysql.connect(host='192.168.2.224', user='root', passwd='password', db='passwords')
cur = conn.cursor()
cur.execute("SELECT * FROM passwords")
for response in cur:
    print(response)
cur.close()
conn.close()


class SQL:
    def __init__(self, username, password, database, host):
        self.username = username
        self.password = password
        self.db = database
        self.host = host
        self.connection = pymysql.connect(host=self.host,
                                          user=self.username,
                                          password=self.password,
                                          db=self.db)

        self.cursor = self.connection.cursor()

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor

    def __del__(self):
        self.cursor.close()
        self.connection.close()



def read_files(file_paths):
    sql = SQL(username="root", password="password", database="passwords", host="192.168.2.224")
    for file in file_paths:
        pf = PasswordFile(path=file, sql=sql)



