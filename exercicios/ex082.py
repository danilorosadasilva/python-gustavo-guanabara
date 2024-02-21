lista = []
while True:
    lista.append(int(input('Incira o valor: ')))
    saida = str(input('Quer sair[S/N]: ')).strip().upper()[0]
    if saida == 'S':
        break
par = []
impar = []
for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'A lista completa é: {lista}')
print(f'Os itens da lista par sao: {par}')
print(f'Os itens da lista impar sao: {impar}')
