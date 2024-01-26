#soluçao do guanabara

valor = int(input('Dijite o quanto voce quer tirar do banco:'))
total = valor
cedula = 50
total_de_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_de_cedula += 1
    else:
        if total_de_cedula > 0:
            print(f'Total de {total_de_cedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_de_cedula = 0
        if total == 0:
            break
print('fim')