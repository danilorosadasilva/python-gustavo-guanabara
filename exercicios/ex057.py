# programa que leia o sexo de uma pessoa, mas so aceita 
# os valores m ou f ,  caso esteja errado , pessa a digitaçao novamente

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, por favor, incira um dado valido [M/F]: ')).strip().upper()[0]
if sexo in 'Mm':
    sexo = '\033[32mMasculino\033[m'
else:
    sexo = '\033[32mFeminino\033[m'
print('Seu da foi salvo como {}'.format(sexo))

''' MEU PROGRAMA
nome = ''
while nome != 'M' and nome != 'F':
    nome = str(input('Qual o seu sexo[M/F]: ')).upper()
    if nome != 'M' and nome != 'F':
        print('tente de novo ....')
print('Fim')'''