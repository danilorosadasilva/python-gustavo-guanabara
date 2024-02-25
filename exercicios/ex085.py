numeros = [[], []]

for i in range(7):
    per  = int(input('Dijite um numero: '))
    if per % 2 == 0:
        numeros[0].append(per)
    else:
        numeros[1].append(per)

numeros[0].sort()
numeros[1].sort()
print(f'Os numeros impares sao: {numeros[1]}')
print(f'Os numeros pares sao: {numeros[0]}')