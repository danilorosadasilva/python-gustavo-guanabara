lista = []
count = 0
while True:
    lista.append(int(input('Digite o numero: ')))
    count += 1
    res = str(input('Terminar:[S/N] ')).strip().upper()
    if res == 'S':
        break
print(f'{count} numeros foram digitados')
lista.sort(reverse=True)
print(f'A lista em valores decressentes: {lista}')
if 5 in lista:
    print('5 esta na lista')
else:
    print('5 nao esta na lista')