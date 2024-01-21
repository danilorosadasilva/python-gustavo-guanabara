#Programa que leia 2 numeros inteiros e mostre na tela:
# o primeito valor e maior
# o segundo valor e menor
# nao exite valor maior e menos, eles sao iguais
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 < n2:
    print('O segundo numero é o maior.')
elif n2 < n1:
    print('O primeiro numero é o maior.')
else:
    print('Os dois sao iguais.')