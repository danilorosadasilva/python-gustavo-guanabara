
n = int(input('dijite um numero:'))
soma = 1
while n != 0:
    soma = soma * n
    n -= 1
print('O fatorial de {} é {}'.format(n, soma))
print('fim')
