import sys
from typing import List, Dict
from pathlib import Path
from main import SQL


class PasswordFile:
    def __init__(self, path: str, sql):
        self.path = path
        self.collection = Path(self.path).parent.name
        self.parse_file(sql)
        sql.connection.commit()

    def parse_file(self, sql : SQL):
        with open(self.path, 'r') as this_file:
            for line in this_file:
                separator = self.best_separator(line)
                query = "INSERT INTO passwords values (NULL, %s, %s, %s)"
                username, password = line.split(separator)

                sql.cursor.execute(query, (username, password, self.collection))


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
    file = PasswordFile(path="../testdata.txt")
