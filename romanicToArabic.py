#Перевод римских цифр в арабские

#Формирование словаря для сопоставления римских цифр с арабскими
dic_roman_years = {
    'I': '1',
    'V': '5',
    'X': '10',
    'L': '50',
    'C': '100',
    'D': '500',
    'M': '1000'
}

#Ввод числа в римской нотации
num = input('Введите год в римской нотации: ')
#Инициация счетчика
dic = 0

#Задание цикла на распознавание введенного римского числа
for i in range(len(num) - 1):
    #Если первое число меньше меньше последующего, то формирование 4 и 9
    if int(dic_roman_years[num[i]]) < int(dic_roman_years[num[i + 1]]):
        dic = dic - int(dic_roman_years[num[i]])
    #Иначе просто складываем число
    elif int(dic_roman_years[num[i]]) >= int(dic_roman_years[num[i + 1]]):
        dic = dic + int(dic_roman_years[num[i]])

dic = dic + int(dic_roman_years[num[len(num) - 1]])

print(dic)