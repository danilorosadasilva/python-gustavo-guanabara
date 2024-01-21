from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada?'))
print('JÔ')
sleep(1)
print('QUEN')
sleep(1)
print('PÔ!!!!')
print('-'*45) 
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-'*45)
#print(itens[computador]) INTERESSANTE
if computador == 0: #pedra
    if jogador == 0:
        print('enpatamos')
    elif jogador == 1:
        print('perdi')
    elif jogador == 2:
        print('ganhei')
    else:
        print('valor invalido')
elif computador == 1: #papel
    if jogador == 0:
        print('ganhei')
    elif jogador == 1:
        print('empatamos')
    elif jogador == 2:
        print('perdi')
    else:
        print('valor invalido')
elif computador == 2: #tesoura
    if jogador == 0:
        print('ganhei')
    elif jogador == 1:
        print('perdi')
    elif jogador == 2:
        print('empatamos')
    else:
        print('valor invalido')
else:
    print('Valor invalido')