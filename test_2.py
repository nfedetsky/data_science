s = int(input('Введите любое целое число: '))
#x = int(s)
for k in range(1, s + 1):
    for n in range(k, k * s + 1, k):
        if n < 10:
            print('|   %d    |' % (n), end='\t')
        elif n < 100:
            print('|  %d    |' % (n), end='\t')
        elif n < 1000:
            print('| %d    |' % (n), end='\t')
        else:
            print('| %d   |' % (n), end='\t')

    print()