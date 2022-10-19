num = int(input('Введите любое целое число: '))
x = int(len(str(num)))
#Определяем длину введенного числа
if x < 6:
    while x < 6:
        if (x % 2 == 0) and (x > 2):
            n = list(str(num))
            n.insert(0, 0)
            n.append(0)
            x = int(len(n))

        elif (x % 2 == 0) and (x == 2):
            n = list(str(num))
            n.insert(0, 0)
            n.insert(0,0)
            n.append(0)
            n.append(0)
            x = int(len(n))

        elif x % 3 == 0:
            n = list(str(num))
            n.insert(0, 0)
            n.insert(0, 0)
            n.append(0)
            x = int(len(n))

        elif x == 5:
            n = list(str(num))
            n.insert(0, 0)
            x = int(len(n))

        else:
            print('Нет решения')
            n = list(str(num))
            for i in range(1, 6):
                n.append(0)
            x = int(len(n))

    sum1 = int(n[0]) + int(n[1]) + int(n[2])
    print('Сумма первых трех цифр равна: ', sum1)

    sum2 = int(n[x-1]) + int(n[x-2]) + int(n[x-3])
    print('Сумма последних трех цифр равна: ', sum2)
    if sum1 == sum2:
        print('Поздравляем! У вас счастливый билет!')
    else:
        print('Весьма сожалеем, у вас билет несчастливый')

else:
    n = list(str(num))
    x = int(len(n))
    sum1 = int(n[0]) + int(n[1]) + int(n[2])
    print('Сумма первых трех цифр равна: ',sum1)

    sum2 = int(n[x - 1]) + int(n[x - 2]) + int(n[x - 3])
    print('Сумма последних трех цифр равна: ', sum2)
    if sum1 == sum2:
        print('Поздравляем! У вас счастливый билет!')
    else:
        print('Весьма сожалеем, у вас билет несчастливый')





