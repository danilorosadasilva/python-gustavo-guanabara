from random import sample
from time import sleep

print("palpites da mega sena".center(50, '-'))

td = list(range(1, 61))

palpites = []

quant = int(input('Quantos palpites? '))

for i in range(quant):
    palpites.append(sample(td, 6))

for ind, i in enumerate(palpites):
    i.sort()
    print(f'palpite {ind+1} : {i}')
    sleep(1)