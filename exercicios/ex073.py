tuplas = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos','Goiás', 'Coritiba','América-MG')

print('=-'*20)

print(f'Os 5 primeiros sao : {tuplas[:5]}')
print('=-'*20)

print(f'Os 4 ultimos sao : {tuplas[-4:]}')
print('=-'*20)

print(f'Em ordem alfabetica: {sorted(tuplas)}')
print('=-'*20)

print(f'Posiçao do Flamengo é a : {tuplas.index('Flamengo')+1}')

print('=-'*20) 