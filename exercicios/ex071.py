print('--------banco-------')
from time import sleep
count_50 = count_20  = count_10 = count_1 = dinheiro2 = 0
dinheiro = int(input('Digite quantos quer sacar: '))
while True:
    if dinheiro >= 50:
        count_50 += 1
        dinheiro -= 50
    elif dinheiro >= 20:
        count_20 += 1
        dinheiro -= 20
    elif dinheiro >= 10:
        count_10 += 1
        dinheiro -= 10
    else:
        count_1 += 1
        dinheiro -= 1
    if dinheiro == 0:
        break
print(f'{count_50:<4} cedulas de 50 Reais')
print(f'{count_20:<4} cedulas de 20 Reais')
print(f'{count_10:<4} cedulas de 10 Reais')
print(f'{count_1:<4} moeda de 1 real')