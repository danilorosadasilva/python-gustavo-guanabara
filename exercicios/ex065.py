maior = menor = num = soma = count = 0
while True:
    num = int(input('Digite um numero: '))
    count += 1
    soma += num
    per = str(input('Quer continuar[S/N]: ')).lower().split()[0]
    if per == 'S':
        break
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / count
print('A media é {}, e o maior é {}'.format(media,maior))


