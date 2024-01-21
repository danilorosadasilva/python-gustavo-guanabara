# calcular o preço da passagem do ônibus
#R$ 0,50 por km viagem ate 200km
#R$ 0,45 para uma viagem acima de 200km

usuario = float(input('Quantos km vai ser sua viagem => '))
if usuario > 200:
    print('Sua viagem vai custar R$ {:.2f}'.format(usuario * 0.45))
else:
    print('sua viagem vai custar {:.2f}'.format(usuario * 0.5))

# da para declarar variavel dentro do if