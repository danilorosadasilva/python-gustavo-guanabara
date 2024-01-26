print('--------banco-------')
count_nota = 0
cedula = 50
dinheiro = int(input('Digite quantos quer sacar: '))
while True:
    if dinheiro >= cedula:
        dinheiro -= cedula
        count_nota += 1
    else:
        if count_nota > 0:
            print(f'{count_nota} cedulas de R${dinheiro}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        count_nota = 0
        if dinheiro == 0:
            break
print('fim')