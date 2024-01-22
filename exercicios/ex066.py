n = count = soma = 0
while n != 999:
    n = int(input('digite o numero: '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'Foram {count} e a soma entre eles foram de {soma}')