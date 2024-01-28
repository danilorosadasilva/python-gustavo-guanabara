tuplas = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis','dezesete', 'dezoito', 'dezenove', 'vinte')
n = 0
while True:
    n = int(input('Digite um numero de 1 a 20:'))
    if n > 0 or n < 21:
        break
    print('tente novamente....')
print(f'Voce digitou o numero: {tuplas[n]}')