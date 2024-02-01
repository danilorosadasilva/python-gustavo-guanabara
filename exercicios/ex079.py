lista = []
while True:
    add = int(input('Digite o numero: '))
    print(add in lista)
    if add in lista:
        print('Ja existe esse item')
    if add not in lista:
        lista.append(add)
    per = str(input('Quer terminar:[S/N] ')).strip().upper()
    if per == 'S':
        break
print(lista)