matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Valor para [{l}:{c}]: '))

print('-'*30)
for i in matriz:
    print(f'[ {i[0]} ] [ {i[1]} ] [ {i[2]} ]')

    # soma de numeros pares
    for n in i:
        if n % 2:
            soma = soma + n

    # a soma dos numeros da terceira
    soma2 = soma2 + i[2]

    # o maior da linha 2
    if i == 1:
        maior_n = max(i)

print(f'A soma de todos os numeros pares são {soma}')
print(f'A soma de todos os numeros da terceira coluna são{soma2}')
print(f'O maior numero da 2 linha é {maior_n}')