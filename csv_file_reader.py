"""
read CSV file into array
"""

import csv
import os.path
from typing import Any


class CsvFileReader:
    @staticmethod
    def read_file(filename: str, skip_header=True) -> list[Any]:
        path = "./" + filename
        if not CsvFileReader.is_csv(path):
            raise OSError('Given file name has to have .csv extension: ' + path)

        if not CsvFileReader.exists(path):
            raise FileNotFoundError('No such file or directory:' + path)

        data = []

        with open(path, 'r') as file:
            csvreader = csv.reader(file)

            if skip_header:
                next(csvreader, None)  # skip the headers

            for row in csvreader:
                data.append(row)

        return data

    @staticmethod
    def is_csv(filename: str) -> bool:
        return filename.endswith(".csv")

    @staticmethod
    def exists(filename: str) -> bool:
        return os.path.isfile(filename)
