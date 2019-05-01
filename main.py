import sys
from pathlib import Path
from classes.SQL import SQL
from classes.password_file import PasswordFile
import threading


if __name__ == '__main__':
    sqlconnection = SQL(username="root", password="password", database="passwords", host="192.168.2.224")
    try:
        startingdir = sys.argv[1]
    except:
        print("Please provide a starting directory\ne.g. " + sys.argv[0] + " /media")
        sys.exit(-1)

    startingdir = Path(startingdir)
    files = list(startingdir.rglob("*.[tT][xX][tT]"))
    threads = []
    for file in files:
        t = threading.Thread(target=PasswordFile, args=(file, sqlconnection))
        threads.append(t)
        t.start()
        

