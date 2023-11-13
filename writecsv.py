import csv
import random

def init(path='positions.csv'):
    fields = ['x', 'y']
    with open(path, 'w') as file:
        csv_writer = csv.DictWriter(file, fields)
        csv_writer.writeheader()

def write(x, y, path='positions.csv'):
    fields = ['x', 'y']
    with open(path, 'a') as file:
        csv_writer = csv.DictWriter(file, fields)
        csv_writer.writerow({'x': x, 'y': y}) 