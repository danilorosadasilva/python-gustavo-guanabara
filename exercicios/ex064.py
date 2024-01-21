n = 0
count = 0
soma = 0
while n != 999:
    count += 1
    soma = soma + n
    n = int(input('dijite o numero: '))
print('{} foram digitados, a soma entre eles e de {}'.format(count, soma))