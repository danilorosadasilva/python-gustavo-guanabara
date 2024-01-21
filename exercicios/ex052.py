#errado
n = int(input('numero: '))
cont = 0
for i in range(1,n+1):
    if n % i == 0:
        cont += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO numero {} foi divisivel {} veses'.format(n,cont))
if cont == 2:
    print('E primo')
else:
    print('nao e primo')