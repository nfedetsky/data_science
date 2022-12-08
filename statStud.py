#Задача по использованию сторонних модулей
import urllib.request as u
import csv
import numpy as np
import matplotlib.pyplot as mpl
import requests as rk

#Объявление пустых словаря и двух списков
d = {}
oblast = []
people = []

#Определение ссылки на файл
urlfile = 'https://minobrnauki.gov.ru/upload/iblock/da3/da3a785a5f70a328ba8171ef3e10f79a.csv'

#Определяем запрос на получение данных с помощью метода get библиотеки requests
response = rk.get(urlfile)
#С помощью urlib копируем структуру скачанного файла в локальный файл
u.urlretrieve(urlfile, 'students.csv')
#Проверка доступности файла
if response.status_code == 200:
    #Открытие локального файла на запись
    with open('students.csv', 'wb') as dt:
        #Записываем данные из сетевого файла в локальный
        dt.write(response.content)
#Открываем сформированный локальный файл на чтение
with open('students.csv', 'r') as file_stud:
    #С помощью библиотеки csv считываем данные и разделяем их по символу ';'
    file = list(csv.reader(file_stud, delimiter=';'))
    #Разделяем данные Регионы отдельно, данные отдельно
    for line in file:
        key = line[0]
        value = line[1:]
        #Фильтруем регионы - отделяем регионы от округов
        if key[0] == ' ':
            #Формирование словаря и списков (для эксперимента)
            k = key.lstrip()
            d[k] = value[6]
            oblast.append(k)
            people.append(value[6])

#Формирвоание гистограммы по полученным данным
mpl.bar(oblast, people, align='center')
mpl.ylabel('Количество учащихся')
mpl.title('Регионы')
mpl.show()