import sys
from typing import List, Dict
from pathlib import Path

from classes.SQL import SQL


class PasswordFile:
    def __init__(self, path: Path, sql):
        self.path = path
        self.collection = self.path.parent.name
        self.sql = sql

    def do_work(self):
        self.parse_file(self.sql)
        sql.connection.commit()

    def parse_file(self, sql : SQL):
        print("Starting")
        with self.path.open('r') as this_file:
            for line in this_file:
                separator = self.best_separator(line)
                query = "INSERT INTO passwords values (NULL, %s, %s, %s)"
                try:
                    username, password = line.split(separator, maxsplit=1)

                    sql.cursor.execute(query, (username, password, self.collection))
                except ValueError:
                    print("Could not parse:\n\t"+line, file=sys.stderr)

    @staticmethod
    def best_separator(line: str, separators=None, type: str = "FIRST"):
        if separators is None:
            separators = [";", ":"]

        indexes: Dict[str, int] = {}
        for separator in separators:
            index = line.find(separator)
            if index < 0:
                index = sys.maxsize
            indexes[separator] = index

        if type is "FIRST":
            return min(indexes, key=indexes.get)
        elif type is "LAST":
            return max(indexes, key=indexes.get)
        else:
            print("type variable to the function best_separator is either FIRST or LAST")



if __name__ == '__main__':
    test = "barsik.ukushevich@mail.ru:nyancatiloveyou:3"
    username, password = test.split(PasswordFile.best_separator(test), 1)
    print(username)
    print(password)
