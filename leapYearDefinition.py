#Определение високосного года

y = int(input('Введите год больше 1900: '))

if y < 1900:
    print('Введенное значение меньше условного')
elif (y % 100 == 0) and (y % 400 == 0):
    print('веденный год является високосным')
elif (y % 100 == 0) and (y % 400 != 0):
    print('Введенный год не является високосным')
elif (y % 400 == 0) or (y % 4 == 0):
    print('Введенный год является високосным')
else:
    print('Введенный год не является високосным')