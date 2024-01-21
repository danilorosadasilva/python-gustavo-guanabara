nota1 = float(input('nota1:'))
nota2 = float(input('nota2:'))
media = (nota1 + nota2) / 2
print('a sua media é: {}'.format(media))
if 7 > media > 5:
    print('Ta de recuperaçao.')
elif media > 6.9:
    print('Aprovado.')
else:
    print('Ta reprovado.')