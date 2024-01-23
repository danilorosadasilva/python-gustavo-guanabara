sexo = '0'
res = '0'
count_idade = count_sexo = count_mais_20 = 0
idade = 0
while True:
    print(f'{'reponda':-^30}')
    idade = int(input('Idade: '))

    if idade >= 18:
        count_idade += 1
        
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()
        if sexo == 'M':
            count_sexo += 1
        elif sexo == 'F' and idade <= 20:
            count_mais_20 += 1

    while res not in 'SN':
        res = str(input('Continuar[S/N]: ')).strip().upper()
    if res == 'N':
        break
    
print(f'{count_idade} pessoas mais de 18 anos')
print(f'{count_sexo} pessoas sao homens')
print(f'{count_mais_20} pessoas sao mulheres e tem menos de 20 anos')
