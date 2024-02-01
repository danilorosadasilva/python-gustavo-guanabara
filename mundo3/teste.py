#---------listas-------------
num = [1, 2, 3, 4]
num[2] = 3 #substituir
num.append(7) # adicionar
num.sort() # ordena alista
num.sort(reverse=True) # ordena a lista reverso
num.pop(1) # apagar itens
num.insert(1) # apaga itens
if 4 in num: # melhor foma de faser
    num.remove(4)

for c , v in enumerate(num): # o enumerate pega tanto o indice, quanto o valor.
    print(f'na posiçao {c} encontrei o valor {v}!')
