print('_|'*42)
print('_|'*42)
print(f'{'MERCADO-DO-DANILO':-^42}')
setup = ('Teclado Gamer', 50,
        'Mouse Gamer', 70,
        'Controle', 2.50,
        'Monitores', 700,
        'Webcam', 300,
        'Headset', 800,
        'Mesa Gamer', 1986,
        'Cadeira Gamer',520)
for iten in range(len(setup)):
    if iten % 2 == 0:
        print(f'{setup[iten]:.<30}', end='')
    else:
        print(f'{setup[iten]:>7.2f}R$')
print(f'{'':-^42}')