#Форматирование таблицы умножения
#Ввод числа
s = int(input('Введите любое целое число: '))

if s:
    #Задаем форматирование верхней таблици
    if s < 1:
        print('Вы ввели число меньше 1')
    elif s > 1:
        print('-' * (9 * s))
        print('||', end='')
        for i in range(1, s + 1):
            if s > 9:
                print('  %d    |' % (i), end='')
            else:
                print('  %d   |' % (i), end='')
        print(' ')
        print('-' * (9 * s))
        #Цикл расчета таблицы умножения и формирвоание таблицы, куда выводим результат расчета
        for k in range(1, s + 1):
            print('|', end='')

            for n in range(k, k * s + 1, k):

                if n < 10:
                    print('   %d    |' % (n), end='')

                elif n < 100:
                    print('   %d   |' % (n), end='')

                elif n < 1000:
                    print('  %d   |' % (n), end='')

                else:
                    print(' %d   |' % (n), end='')

            print(' ')

        print('_' * (9 * s))
    else:
        print('Введите число')
