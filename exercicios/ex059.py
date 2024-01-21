from time import sleep
from random import randint
menu ='''-------MENU----------
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA'''
opiçoes = 0
soma = 0
while opiçoes != 5:
    print(menu)
    opiçoes = int(input('OPÇâO => '))
    if opiçoes == 1:
        n1 = int(input('1ª numero: '))
        n2 = int(input('2ª numero: '))
        print('-'*40)
        print('A soma é: {}'.format(n1 + n2))
    if opiçoes == 2:
        n1 = int(input('1ª numero: '))
        n2 = int(input('2ª numero: '))
        print('-'*40)
        print('A multiplicaçao é {}'.format(n1 * n2))
    if opiçoes == 3:
        print('Desculpe, eu nao fui faito para faser isso.')
    if opiçoes == 4:
        print(randint(1,10))
    sleep(1)
    print('='*40)
print('fim do programa')