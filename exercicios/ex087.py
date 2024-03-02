lista_das_coisas = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
lista = [[],[],[]]
count = 0
soma = soma2 = 0

for ind,i in enumerate(lista_das_coisas):
    for i2 in i:
        if i2 % 2 == 0:
            soma = soma + i2
    if ind % 3 == 0 and ind != 0:
        count += 1
    lista[count].append(int(input(f'Dijite um valor para {i}: ')))


print('-'*30)
for i in lista:
    print(f'[ {i[0]} ] [ {i[1]} ] [ {i[2]} ]')
    soma2 = soma2 + i[2]
    if i == 1:
        maior_n = max(i)

print(f'A soma de todos os numeros pares são {soma}')
print(f'A soma de todos os numeros da terceira coluna são {soma2}')
print(f'O maior numero da 2 linha é {maior_n}')