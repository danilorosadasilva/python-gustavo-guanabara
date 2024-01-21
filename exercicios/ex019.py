#sortear 4 nomes
from random import choice
n1 = str(input('Digite o nome: '))
n2 = str(input('digite o nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite o nome: '))
nomes =  [n1, n2, n3, n4]
print('-' * 30)
print('O nome sorteado foi : {}'.format(choice(nomes)))
print('-' * 30)