#Программа, перемешивающая буквы в слове
#Вводим библиотеку random
import random

#Ввод слова
str_1 = input('Введите слово: ')
#Разбиваем слово на буквы
strList = list(str_1)
s = ' '
#Перемешиваем буквы в списке
result = random.sample(strList, len(strList))
#Собираем из букв слово
for i in range(0, len(result)):
    s = s + result[i]
print('Новое слово: ', s)

s = input('Введите слово: ')

str_1 = ' '

for i in range(0, len(s)):
    str_1 = str_1 + s[i] * 2

print('Всем привет!')
print('Модификация слова: ', str_1)