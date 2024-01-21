#ler um nome e mostrar : 
#  o nome com todas as letras minusculas,
#  com otodas as letras maiusculas,
#  quantas letras tem(sem espaço),
#  quantas letras tem o primeiro nome

nome = str(input('Digite qual o seu nome: '))
print('nome em maiusculas: '.format(nome.lower()))
print('Nome em maiusculas: '.format(nome.upper()))
print('seu nometem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O nome {} tem {} letras'.format(separa[0], len(separa[0])))

'''
nome = nome.split()
print('seu primeiro nome tem {} letras'.format(len(nome[0])))
nome = ''.join(nome)
print('Seu nome tem {} letras'.format(len(nome)))'''

