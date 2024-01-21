#programa que aprova um emprestimo bancario
# pergunta o valor da casa
# o salario
# em quantos anos ela vai pagar
# - vai calcular o valor mensal q tera q pagar
# - o valor da pretaçao n pode passar de 30% do salario 
print('{:-^45}'.format('emprestimo bancario'))

valor = float(input('QUAL O VALOR DA CASA: '))
sal = float(input('QUAL O SEU SALARIO: '))
anos = float(input('EM QUANTOS ANOS VAI PAGAR: '))

meses = anos * 12
por = sal - ((sal / 100) * 30)
total_a_pagar = valor / meses

print('POR MES VOCE TERIA QUE PAGAR {:.2f} REAIS POR MÊS'.format(total_a_pagar))

if total_a_pagar <= por:
    print('-------------O seu emprestimo foi aprovado')
else:
    print('-------------Nao foi aprovado')