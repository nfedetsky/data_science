s = input('Введите предложение: ')

lin = s.split()

max_lin = len(lin[0])
max_ar = len(lin)
position = 0
for i in range(0, max_ar):
    if len(lin[i]) > max_lin:
        max_lin = len(lin[i])
        position = i

lt_1 = lin[position]
end_litera = lt_1[max_lin-1]
lt_2 = lin[position + 1]
first_litera = lt_2[0]

if end_litera == first_litera:
    print('Самое длинное слово в массиве: ', lt_1)
    print('Следующее за самым длинным словом, слово: ', lt_2)
    print('Первая буква следующего слова совпадает с последней буквой предыдущего слова', end_litera, '=', first_litera)
else:
    print('Самое длинное слово в массиве: ', lt_1)
    print('Следующее за самым длинным словом, слово: ', lt_2)
    print('Первая буква следующего слова НЕ совпадает с последней буквой предыдущего слова', end_litera, '!=', first_litera)