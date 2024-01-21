# Progressao aritimetica
t1 = int(input('primeiro termo: '))
rasao = int(input('rasao:'))
cont = 0
resut = 0
while cont != 10:
    cont += 1
    resut = rasao + (t1 * (cont-1))
    print(resut, end=' => ')
print('fim')