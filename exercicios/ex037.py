#Programa que leia um numero e converta em:
# - binario
# - octal
# - hexadecimal
num = int(input('Digite um numero inteiro: '))
print('''EScolha uma das base de conversao:
[ 1 ] converter para binario
[ 2 ] converter para octal
[ 3 ] converter para exadecimal''')
opçao = int(input('Sua opçao: '))
if opçao == 1:
    print('{} convertido para binario e igual a \033[32m{}\033[m'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para exadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Valor invalido')