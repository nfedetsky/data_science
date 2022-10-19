#Простейший калькулятор
k = True
while k:
    calc = input('Введите выражение: ')
    x, operand, y = calc.split(' ')
    x = float(x)
    y = float(y)
    if operand == '+':
        print('Ответ: ', x + y)
        n = input('Хотите продолжить? Введите Y или N  ')
        if n == 'Y' or 'y' or 'да' or 'д':
            k = True
        else:
            k = False
    elif operand == '-':
        print('Ответ: ', x - y)
        n = input('Хотите продолжить? Введите Y или N  ')
        if n == 'Y':
            k = True
        else:
            k = False
    elif operand == '*':
        print('Ответ: ', x * y)
        n = input('Хотите продолжить? Введите Y или N  ')
        if n == 'Y':
            k = True
        else:
            k = False
    elif operand == '/':
        if y == 0:
            print('В ввели делитель 0. Решения нет')
            n = input('Хотите продолжить? Введите Y или N  ')
            if n == 'Y':
                k = True
            else:
                k = False
        else:
            print('Ответ: ', x / y)
            n = input('Хотите продолжить? Введите Y или N  ')
            if n == 'Y':
                k = True
            else:
                k = False
    else:
        n = input('')
        if n == 'Y':
            k = True
        else:
            k = False