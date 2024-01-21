#faser o computador pensar em um numero de 0 a 5 e peça pa o
# usuario tentar descobrir qual foi o numero escolhido pelo 
# computador, o programa devera escrever na tela se venceu ou perdeu

from random import randint

'''sorteio = randint(0, 5)
n = int(input('QUAL NUMERO VOCE ACHA QUE VAI SER SORTEADO => '))
if n == sorteio:
    print('VOCE ACERTOU!!!!!!')
else:
    print('VOCÊ ERROU')
'''
from time import sleep #FASER O COMPUTADOR PARA POR SEGUNDOS
print('')                                     #------------------------
computador = randint(0, 5)
print('{:-^55}'.format('começo-do-programa')) #------------------------
print('Vou pensar em um numero entre 0 e 5. Tenre adivinhar ....')
print('-'* 55)                                #-----------------------
print(computador)
jogador = int(input('Escolha o numero: '))
print('PROCESSANDO....')
sleep(20)
if jogador == computador:
    print('PARABENS! Você conseguiu me vencer!')
else:
    print('GANHEI OTARIO! Achou que ia ganhar de mim!?')
print('{:-^55}'.format('fim-do-programa'))
print('')#deixar um espaço a mais depois do programa-------