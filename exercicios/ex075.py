núm = (int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite outro de novo numero: ')),
     int(input('Digite ultimo numero: ')),)
print(f'O 9 apareceu {núm.count(9)} posiçao')
print(f'Posiçao do 3 {núm.index(3)+1}')
print('Os numeros pares sao ',end='')
for i in núm:
    if i % 2 ==0:
        print(i, end=' ')