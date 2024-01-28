núm = (int(input('Digite um numero: ')),
     int(input('Digite outro numero: ')),
     int(input('Digite mais um numero: ')),
     int(input('Digite outro de novo numero: ')),
     int(input('Digite ultimo numero: ')),)
if 9 in núm:
    print(f'O 9 apareceu {núm.count(9)} posiçao')
else:
    print('O valor 9 não foi digitado')
if 3 in núm:
    print(f'Posiçao do 3 é a {núm.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')
print('Os numeros pares sao ',end='')
for i in núm:
    if i % 2 ==0:
        print(i, end=' ')