# Ler o nome completo de uma pessoa e 
# mostre o primeiro nome e o ultimo nome
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0].capitalize()))
print('Ultimo nome: {}'.format(nome[-1].capitalize()))
