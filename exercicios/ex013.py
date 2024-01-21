#faser uma atualizaçao de um salario, com 15% a mais

salario = float(input('Qual o seu salario atual? R$ '))
percentual = salario + (salario / 100 * 15)
print('O seu novo salario é de {} Reais, PARABENS!!!'.format(percentual))

