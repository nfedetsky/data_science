#Статистические показатели

mes = int(input('Ведите количество месяцев: '))
mass = [list(map(int, input('Введите данные за месяц: ').split())) for i in range(mes)]
k = []
count = 0
kol = 0
med = 0.0
#Цикл подсчета общего значения продаж по менеджерам
for i in range(len(mass)):
    for j in range(len(mass[i])):
        kol = kol + mass[i][j]
        count = count + 1
        k.append(mass[i][j])
#Расчет среднего показателя
sred_znach = kol / count

#Подготовка переменных для расчета медианы
k.sort()
a, b = len(k), (len(k) + 1)
print(a, b)
#Расчет медианы для списка с четным количеством элементов и с нечетным количеством элементов
if b % 2 == 0:
    med = (a // 2)
else:
    med = b // 2

print(med)