# Progressao aritimetica
t1 = int(input('primeiro termo: '))
rasao = int(input('rasao:'))
cont = 0
resut = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont != total:
        cont += 1
        resut = rasao + (t1 * (cont-1))
        print(resut, end=' => ')
    print('pausa')
    mais = int(input('Quantos termos voce quer mais? '))
print('Progressao finalizada com {} termos'.format(total))