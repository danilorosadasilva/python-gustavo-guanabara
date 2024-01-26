# Programa  que leia o nome e o preço do produto
# - Qual o total gasto na compra
# - Quantos produtos custam mais de 1000 reais
# - O nome do produto mais barato
nome_do_produto = ter = 'ç'
count = maior = menor = soma_do_preço = mais_de_1000 = 0
print(f'\033[32m{'MERCADO-DO-GUSTAVO-GUANABARA':-^40}\033[m')
while True:
    print(f'----------compra numero: {count+1}----------')
    nome = str(input('Nome do produto: ')).strip().upper()
    preço = int(input('Preço do produto R$: '))
    if preço > 1000:
        mais_de_1000 += 1
    soma_do_preço += preço
    if count == 0 or maior < preço:
        maior = preço
        nome_do_produto = nome
    while ter not in 'SN':
        ter = str(input('terminar[S/N]:')).strip().upper()[0]
    if ter == 'S':
        break
    count += 1
print('-'*30)
print(f'O total da compra ficou em {soma_do_preço}R$')
print(f'{mais_de_1000} é o produto custam mais de 1.000 reais')
print(f'{nome_do_produto} foi o produto mais caro')
print('-'*30)