# ver o comprimento de 3 retas e ver se pode formar um triangulo
r1 = float(input('Digite o comprimento da reta em centimetros => '))
r2 = float(input('Digite o comprimento da reta em centimetros => '))
r3 = float(input('Digite o comprimento da reta em centimetros => '))
l = [r1, r2, r3]
l.sort()
if l[0] + l[1] <= l[2]:
    print('Não da para faser um triangulo.')
else:
    print('Da para faser um triangulo.')
