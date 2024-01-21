#ler 3 numeros e mostre o maior e menor

#---------------MINHA-SOLUÇAO----------------------

print('{:-^20}'.format('começo'))

n1 = int(input('Digite o numero: '))
n2 = int(input('Digite o numero: '))
n3 = int(input('Digite o numero: '))

n = [n1, n2, n3]

print('{:-^20}'.format('resposta'))

print('O maior numero é : {}'.format(max(n)))
print('O menor numero é : {}'.format(min(n)))
if max(n) == min(n):
    print('Os três valores são iguais.')

print('{:-^20}'.format('fim'))
print('')