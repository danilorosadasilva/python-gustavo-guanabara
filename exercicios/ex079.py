lista = []
while True:
    add = int(input('Digite o numero: '))
    if add not in lista:
        lista.append(add)
    else:
        print('Ja exite esse valor...')
    per = str(input('Quer terminar:[S/N] ')).strip().upper()
    if per == 'S':
        break
print(lista)