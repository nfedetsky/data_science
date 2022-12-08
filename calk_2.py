import os

with open(os.path.join('.', 'data.tsv')) as dt:
    for line in dt:
        line = dt.readline().strip().split()
        print(line)