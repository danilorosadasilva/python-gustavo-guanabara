matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matris[l][c] = int(input(f'Valor para [{l}:{c}]: '))

for i in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matris[i][c]:^5} ]', end='')
    print()