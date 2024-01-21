soma = 0
cont = 0
for i in range(0,7):
    n = int(input('numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1

print(soma, cont)