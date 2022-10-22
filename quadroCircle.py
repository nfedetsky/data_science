#Вычисление квадратуры круга

sqCircle = float(input('Введите значение площади круга: '))
sqQudro = float(input('Введите значение площади квадрата: '))

pi = 3.14
diamCicle = ((sqCircle/pi)**(1/2)*2) # вычисляем диаметр круга S=pi*r**2
lineQuadro = sqQudro**(1/2) #вычисляет сторону квадрата L = S**1/2
diagQuadro = (2*lineQuadro**2)**(1/2) #вычисляем диагональ квадрата a**2 + b**2 = c**2

#условия сравнения

if diagQuadro <= diamCicle:
    print('2')
elif lineQuadro >= diamCicle:
        print('1')
else:
    print('0')

print('Диаметр: ', diamCicle)
print('Длина стороны квадрата', lineQuadro)
print('Диагональ', diagQuadro)