line = input() # запрашиваем данные
months = [] # инициализщируем список месяцев, это будет двумерный массив
while len(line): # пока ввод не пустой
    months.append([ int(i) for i in line.split()]) # добавляем в список значения трудочасов
    line = input() # считываем новую строку
if len(months) > 1: # если хотя бы что-то ввели
    month = 0 # текущий месяц, начинаем с первого
    work = [0] * len(months[month]) # пустой список трудочасов по числу инженеров в первом месяце
    while month < len(months): # перебираем месяцы, считаем трудочасы
        engineer = 0 # начинаем с первого инженера
        while engineer < len(months[month]): # перебираем инженеров
            work[engineer] += months[month][engineer] # прибавляем инженеру трудочасы
            engineer += 1 # переходим к следующему инженеру
        month += 1 # увеличиваем месяц
    if work[0] > work[1]:
        if work[0] > work[2]:
            print ("Инженер #1 - ударник труда! Средние трудочасы: " + str(work[0]/len(months)))
        else:
            print ("Инженер #3 - ударник труда! Средние трудочасы: " + str(work[2]/len(months)))
    elif work[1] > work[2]:
        print ("Инженер #2 - ударник труда! Средние трудочасы: " + str(work[1]/len(months)))
    else:
        print ("Инженер #3 - ударник труда! Средние трудочасы: " + str(work[2]/len(months)))
else: # иначе выводим ошибку
    print("Нет данных")