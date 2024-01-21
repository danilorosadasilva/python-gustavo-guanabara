# Progressao aritimetica
t1 = int(input('primeiro termo: '))
rasao = int(input('rasao: '))
termos = int(input('Quantidade de termos: '))
cont = 0
resut = 0
while cont != termos +1:
    cont += 1
    resut = rasao + (t1 * (cont-1))
    print(resut, end=' => ')
print('fim')