# ler um numero inteiro e mostrar se ele é par ou impar
n = int(input('DIGITE UM NUMERO: '))
r = n % 2
if n == 0:
    print('{} è par.'.format(n))
else:
    print('{} è impar.'.format(n))