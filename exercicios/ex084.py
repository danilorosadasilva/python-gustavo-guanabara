dados = []
cadastro = []

while True:
    cadastro.append(input('Nome: '))
    cadastro.append(input('Idade: '))
    cadastro.append(float(input('Peso: ')))
    dados.append(cadastro[:])
    cadastro.clear()
    per = input(str('Quer continuar? [S/N] ')).strip().upper()[0]
    if per == 'N':
        break

print('-'*20)

print(f'Foram cadastradas {len(dados)} pessoas')

maior = menor = 0

for ind, i in enumerate(dados):
    if ind == 0:
        maior = menor = i[2]
    else:
        if i[2] > maior:
            maior = i[2]
        elif i[2] < menor:
            menor = i[2]

for i in dados:
    if i[2] == menor:
        print(f'Os menores pesos sao de {i[0]}')
    elif i[2] == maior:
        print(f'Os maiores sao de de {i[0]}')

print('-'*20)