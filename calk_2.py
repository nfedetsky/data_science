
#mes = int(input('Ведите количество месяцев: '))
#man = int(input('Ведите количество менеджеров: '))
"""
while :
    mass = list(map(int, input('Введите данные за месяц: ').split()))
    if mass == ' ':
        break

    # for i in range(mes)]
    if not mass:
        break

a = []
s = 0
k = 0

k = int(input('Введите к: '))
while True:
    try:
        s = input('Введите аргумент: ').split()
        if not s:
            break
        a.append(s)
    except EOFError:
        break
print(a)
"""
mass = []
i = 0
while True:
    i = input('Введите данные по менеджерам: ').split()
    if not i:
        break
    else:
        mass.append(i)

print(mass)
