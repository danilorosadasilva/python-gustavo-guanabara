from random import randint
n = (randint(1,11), randint(1,11), randint(1,11), randint(1,11), randint(1,11))
print(f'Os numeros sorteados sao: ', end='')
for i in n:
    print(f'{i} ',end='')
print(f'\nO maior numero é {max(n)}')
print(f'O menor numero é {min(n)}')