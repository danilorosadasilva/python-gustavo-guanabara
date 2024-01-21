# nao funciona, espero no futuro entender
soma_idade = 0
media_da_idade = 0
maior_idade_de_homem = 0
nome_do_homem_mais_velho = ''
total_mulher = 0
for p in range(1, 5):
    print('---------{} pessoa ----------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    soma_idade += idade 
    if p == 1 and sexo in 'Mn':
        maior_idade_de_homem = idade
        nome_do_homem_mais_velho = nome
    if sexo in 'Mn' and idade > maior_idade_de_homem:
        maior_idade_de_homem = idade
        nome_do_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1
media_da_idade = soma_idade / 4
print('A media da idade do grupo e de {} anos'.format(media_da_idade))
print('O {} é o homem mais velho, com {} anos'.format( nome_do_homem_mais_velho, maior_idade_de_homem))
print('O total de mulheres com menos de 20 anos sao de {}'.format(total_mulher))