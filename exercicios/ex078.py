lista = []
for i in range(5):
    lista.append(int(input('Digite o valor:')))
print(lista)

maior = lista.index(max(lista))
menor = lista.index(min(lista))

print(f'O maior valor digitado foi {lista[maior]} na posiçao {maior}')
print(f'O menor valor digitado foi {lista[menor]} na posiçao {menor}')


