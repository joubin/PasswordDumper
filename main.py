import sys
from pathlib import Path

import pymysql

import pymysql

from classes.SQL import SQL
from classes.password_file import PasswordFile

# _sqlconnection = None

# def read_files(file_paths):
#     if _sqlconnection is None:
#         _
#     for file in file_paths:
#         pf = PasswordFile(path=file, sql=_sqlconnection)


if __name__ == '__main__':
    sqlconnection = SQL(username="root", password="password", database="passwords", host="192.168.2.224")
    try:
        startingdir = sys.argv[1]
    except:
        print("Please provide a starting directory\ne.g. " + sys.argv[0] + " /media")
        sys.exit(-1)

    startingdir = Path(startingdir)
    files = list(startingdir.rglob("*.[tT][xX][tT]"))
    for file in files:
        pf = PasswordFile(path=file, sql=sqlconnection)
