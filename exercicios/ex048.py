n = 0
cont = 0
for i in range(1,500,2):
    if i % 3 == 0:
        n += i
        cont += 1
print('A soma de todos os \033[32m{}\033[m valores é \033[32m{}\033[m'.format(cont, n))