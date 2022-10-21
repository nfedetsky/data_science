str1 = input('Введите строку: ')
#lit = input('Введите букву, которую требуется найти: ')

if str1:
    k = str1[0]
    print(k)
    for i in str1:
        print(str1[i])
        if k != str1[i]:
            k = str1[i]
            i += i
        else:
            k = k + str(str1.count(k))
print(k)
#print('В веденной строке ', '"', str1, '"', str1.count(lit), ' символов')
