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

print(dados)

for i in dados:
    print(f'{i[0]} tem {i[1]} e pesa {i[2]:.2f}kg')