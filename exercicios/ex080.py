lista = []
for i in range(5):
    lista.append(int(input('Digite um numero: ')))
for n, iten in enumerate(lista):
    if n == 1:
        maior = menor = n