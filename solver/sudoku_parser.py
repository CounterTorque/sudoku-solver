import csv
import io

def parse_sudoku(input_data: str):
    reader = csv.reader(io.StringIO(input_data), delimiter=',')
    for row in reader:
        print(row)