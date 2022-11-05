#Сдвиг массива
#Универсализируем ввод шаг сдвига
k = int(input('Введите количество шагов сдвига: '))
#Генерация списка
s = [i for i in range(1, 25)]
#Копия списка
s_copy = [i for i in s]
#Добавление элементов списка
for i in range(0, k):
    s.append(0)
#Определяем конец массива для функции range
n = len(s) - 1
#Сдвиг массива на k шагов
for i in range(0, k):
    s.insert(i, s.pop(n))
print(s_copy)
print(n)
print(s)
