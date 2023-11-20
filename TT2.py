import os
import urllib.request as u
import csv
import numpy as np
import matplotlib as mpl
import requests as rk

d = {}

urlfile = 'https://minobrnauki.gov.ru/upload/iblock/da3/da3a785a5f70a328ba8171ef3e10f79a.csv'
response = rk.get(urlfile)
#u.urlretrieve(urlfile, 'students.csv')

if response.status_code == 200:
    with open(response, 'r') as dt:
        for line in dt:
            print(line)

"""
for key, value in d.items():
    if key[0] == ' ':
        k = key
        v = value
        b[k] = v
print(b)
"""
"""
for key in d.keys():
    if key[0] == ' ':
        print(key)
"""
"""
    key_split = list(key)
    if key_split[0] == ' ':
        b.append(key)
print(b)
"""
