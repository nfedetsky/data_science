from random import randint

number = [randint(1, 10) for i in range(100)]

max1 = min(number)
max2 = min(number)

for i in number:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2 and i < max1:
        max2 = i

print('Max 1: ', max1, 'Max 2: ', max2)