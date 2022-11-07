from itertools import zip_longest
from random import randint

n = [randint(1, 30) for i in range(0, 20)]

st = list(map(sum, zip_longest(*[[1] * j for j in n], fillvalue=0)))

print(n)
print(st)