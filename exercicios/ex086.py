lista_das_coisas = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
lista = [[],[],[]]
count = 0
for ind,i in enumerate(lista_das_coisas):
    if ind% 3 == 0 and ind != 0:
        count += 1
    lista[count].append(int(input(f'Dijite um valor para {i}: ')))

print(lista)
for i in lista:
    print(i)