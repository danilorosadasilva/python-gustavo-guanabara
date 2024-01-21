#perguntar o salario e calcule o valor do seu aumento:
# PARA SALARIOS SUPERIORES A 1250, 10% DE AUMENTO
# PARA INFERIORES OU IGUAIS, O AUMENTO É DE 15%
sal = float(input('DIGITE O VALOR DOS SEU SALARIO: '))
if sal <= 1250:
    sal = sal + (sal * 15 / 100)
else:
    sal = sal + (sal * 10 / 100)
print('O sue novo salario é {}'.format(sal))