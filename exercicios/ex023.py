#ler unidades desena e centenas
num = int(input('Digite o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('UNIDADE: {}'.format(u))
print('DESENA : {}'.format(d))
print('CENTENA: {}'.format(c))
print('MILHAR : {}'.format(m))
