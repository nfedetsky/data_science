#Статистические показатели

mes = int(input('Ведите количество месяцев: '))
mass = [list(map(int, input('Введите данные за месяц: ').split())) for i in range(mes)]

count = 0
kol = 0
#Цикл подсчета общего значения продаж по менеджерам
for i in range(len(mass)):
    for j in range(len(mass[i])):
        kol = kol + mass[i][j]
        count = count + 1
#Расчет среднего показателя
sred_znach = kol / count

