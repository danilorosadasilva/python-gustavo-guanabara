n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('_'*20)
print('A soma é: {},\nO produto é: {}\nE adivisão é: {}'.format(s, m, d), end=', ')
print('Divisão inteira é: {} \nA potência é: {}'.format(di, e))