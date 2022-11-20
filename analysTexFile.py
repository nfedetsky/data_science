#Студни
"""
Программа получилась, взможно, громоздкой - здесь нужна помощь лида, чтобы он указал, что и как поправить или сделать по-другому,
более оптимально.
Позволил себе несколько отойти (возможно) от условия и несколько расширил его. Т.к. в условии задачи четко не сказано по каким объектам
делать расчет качества знаний и обученность, то я расширил условия самостоятельно. Во-первых, расчет справедлив, и для каждого студента в частности,
и для группы студентов в целом. Я сделал эти расчеты и вывел в табличном виде. Во-торых, ставя себя на место Заказчика, я бы попросил детализацию данных,
что и сделал.
Есть еще один нюанс - 1 и 2 пп. говорят о жетском условии: "оценка больше...", "оценка меньше...". Я так и сделал.
Если поставить мягкое условие ">=", то будут считаться успевающими три студента - сейчас два.

"""
import os

#Инициация словарей
#Генерация словаря оценок для расчета статисчетов
b = {k: 0 for k in ['5', '4', '3', '2', '1']}
d = {}
#Открытие файла
with open(os.path.join('.', 'data.tsv')) as dt:
    #Для удобства работы с данными, формируем словарь
    for line in dt:
        #Построчно формируем словарь
        line = dt.readline().strip().split()
        for l in line:
            key = line[0]
            value = line[1:]
            d[key] = value
#Делаем копию словаря для расчета стат данных пофамильно
d_copy = dict(d)

#Цикл для получения средних оценок студентов
for i in d:
    #Инициация переменных итерации
    ls = 0
    #Присваиваем переменной значение текущего ключа
    arr = d.setdefault(str(i))
    #Получаем количество элементов (количество оценок текущего студента)
    ls = len(arr)
    summ = 0
    res = 0
    for j in arr:
        #Суммируем все оценки текущего студента
        summ = summ + int(j)
        #Получаем среднюю оценку успеваемости текущего студента
        res = round(summ / ls, 2)
        #Дополнительно, в цикле поучаем данные о количестве каждой из оценок
        if j == '5':
            b[j] += 1
        elif j == '4':
            b[j] += 1
        elif j == '3':
            b[j] += 1
        elif j == '2':
            b[j] += 1
        elif j == '1':
            b[j] += 1
    #Формирование нового словаря на основе старого
    d[i] = res

#Вывод списка успеваемости студентов в табличном виде
print('Список успевающих студентов:')
print('-' * (7 * 5))
print('|', end='')
print('  Студент    |', end='')
print('   Средняя оценка  ',end='')
print('|')
print('-' * (7 * 5))
for stud in d.items():
    if stud[1] > 4.5:
        if len(stud[0]) < 10:
            print('|', end='')
            print('  %s   |' % (str(stud[0])), end='')
            print('        %s  ' % (str(stud[1])), end='')
            print('     |')
            print('-' * (7 * 5))
        else:
            print('|', end='')
            print('  %s |' % (str(stud[0])), end='')
            print('        %s  ' % (str(stud[1])), end='')
            print('     |')
            print('-' * (7 * 5))

print('Список студентов на отчисление:')
print('-' * (7 * 5))
print('|', end='')
print('  Студент    |', end='')
print('   Средняя оценка  ',end='')
print('|')
print('-' * (7 * 5))
for stud in d.items():
    if stud[1] < 2.5:
        if len(stud[0]) < 10:
            print('|', end='')
            print('  %s   |' % (str(stud[0])), end='')
            print('        %s  ' % (str(stud[1])), end='')
            print('     |')
            print('-' * (7 * 5))
        else:
            print('|', end='')
            print('  %s |' % (str(stud[0])), end='')
            print('        %s  ' % (str(stud[1])), end='')
            print('     |')
            print('-' * (7 * 5))
    else:
        continue

print('\n')

#Средняя оценка успеваемости студентов
so = round(sum(d.values()) / len(d), 2)
print('Средняя оценка успеваемости студентов: ', so, '\n')

#Расчет и запись в файл процента успеваемости выше среднего
count = 0
#Открываем файл result.txt на запись
with open('result.txt', 'w') as result:
    #Проводим расчет количества студентов, чья успеваемость выше среднего в процентах
    for i in d.values():
        if i > so:
            count = count + 1
    proc = (count * 100) / len(d)
    #Запись результатов расчета в файл
    result.write('Процент студентов, чей средний балл выше среднего, равен: ')
    result.write(str(int(proc)))

#Определение качества обученности каждого студента
#Инициация переменных для расчета статистических данных (качество и обученность) по группе
glob_s5 = 0
glob_s4 = 0
glob_s3 = 0
glob_s2 = 0
glob_s1 = 0
#Начинаем цикл для расчета стат данных по каждому студенту и по группе в целом
for i in d_copy.items():
    #Определяем и инициируем перменные для проведения подсчета результатов успеваемости по каждому студенту и группе в целом
    k = i[0]
    v = i[1]
    l = len(v)
    s5 = 0
    s4 = 0
    s3 = 0
    s2 = 0
    s1 = 0
    for j in v:
        if j == '5':
            s5 = s5 + int(j)
            glob_s5 = glob_s5 + int(j)
        elif j == '4':
            s4 = s4 + int(j)
            glob_s4 = glob_s4 + int(j)
        elif j == '3':
            s3 = s3 + int(j)
            glob_s3 = int(j)
        elif j == '2':
            s2 = s2 + int(j)
            glob_s2 = int(j)
        elif j == '1':
            s1 = s1 + int(j)
            glob_s1 = int(j)
    #Расчет качества и обученности студента по методу академика Б.П.Смирнова
    s_kach = (s5 + s4) / l
    s_ob = (s5 * 1 + s4 * 0.64 + s3 * 0.36 + s2 * 0.16 + s1 * 0.08) / l
    #Формируем словарь с данными о качестве и обученности каждого студента
    d_copy[k] = round(s_kach, 2), round(s_ob, 2)

#Расчет качества и обученности группы по методу академика Б.П.Смирнова
glob_s_kach = (glob_s5 + glob_s4) / len(d)
glob_s_ob = (glob_s5 * 1 + glob_s4 * 0.64 + glob_s3 * 0.36 + glob_s2 * 0.16 + glob_s1 * 0.08) / len(d)

#Ввывод результатов статистических расчетов в табличном виде
print('Таблица качества и обученности студентов')
print('-' * (9 * 6))
print('|', end='')
print('  Студент    |', end='')
print('   Качество обучения  |', end='')
print('  Обученность  ', end='')
print('|')
print('-' * (9 * 6))

for i in d_copy.items():
    k = i[0]
    v = i[1]
    if len(k) < 10:
        print('|  %s   |' % (k), end='')

    else:
        print('|  %s |' % (k), end='')
    if len(str(v[0])) < 4:
        print('         %s          |' % (str(v[0])), end='')
        print('      %s     |' % (str(v[1])))
        print('-' * (9 * 6))
    else:
        print('         %s         |' % (str(v[0])), end='')
        print('      %s     |' % (str(v[1])))
        print('-' * (9 * 6))

print('Показатель качества обучения группы: ', round(glob_s_kach, 2))
print('Показатель обученности группы: ', round(glob_s_ob, 2), '\n')
print('Процентный показатель успеваемости записан в файл result.txt')
