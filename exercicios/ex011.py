# ler a largura e a altura de uma paprede, calcular a area
# e a quantidade de tinta para para pintar, sabendo que cada litro 6.25
# pinta 2m quadrado

print('-' * 45)

alt = float(input('qual a altura?  '))
lar = float(input('qual a largura?  '))
tinta = lar * alt / 2
print('Voce precisa de {} litros para pintar essa parede.'.format(tinta))

print('-' * 45)