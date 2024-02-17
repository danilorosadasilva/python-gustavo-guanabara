print('- '*30)

lista = []
maior = 0
menor = 0
for i in range(5):
    lista.append(int(input(f'Digite o {i} valor:')))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]

print('- '*30)

print(f'Voce digitou os valores: {lista}')
print(f'O maior valor foi {maior} nas posiçoes ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}...', end='')
print()
print(f'O menor valor foi {menor} nas posiçoes ',end='')

for i, v in enumerate(lista):
    if v == menor:
        print(f' {i}...', end='')




