import csv
import random

def init(path='positions.csv'):
    fields = ['x', 'y']
    with open(path, 'w') as file:
        csv_writer = csv.DictWriter(file, fields)
        csv_writer.writeheader()

def write(x, y, x0=0, y0=0, path='positions.csv'):
    # we writing x,y only if its not the same as prev point
    fields = ['x', 'y']
    if x!=x0 and y!=y0:
        with open(path, 'a') as file:
            csv_writer = csv.DictWriter(file, fields)
            csv_writer.writerow({'x': x, 'y': y}) 
    return x,y