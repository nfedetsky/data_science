# Приведение введенного числа к четырем типам

a = input('Введите любое число: ')

print('Вывод в виде целого числа: ', int(a))
print('Вывод  в виде вещественного числа: ', float(a))
print('Вывод в виде строки (функция input возвращает строковое значение): ', a)
print('Но можно и так вывести, с кавычками, как в примере: ', '"', a, '"')
print('Вывод преобразования в логический тип: ', bool(a))