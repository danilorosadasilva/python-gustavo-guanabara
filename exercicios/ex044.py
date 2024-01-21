# programa que calcule o valor a ser pago no produto conciderando o preço normal e condiçao de pagamento
# - a vista dinheiro/cheque : 10% de desconto
# - a vista no cartao : 5% de desconto
# - em ate 2x no cartao : preço normal
# - 3x ou mais no cartao: 20% de juros
print('''
NO CARTAO(1)
NO CHEQUE(2) 
OU NORMAL(3)''')
forma_de_pag = int(input('SUA RESPOSTA: '))
preço = float(input('DIGITE O PREÇO: '))

if forma_de_pag == 1:
    quan = int(input('EM QUANTAS VESES?  '))
    if quan > 0 and quan < 3:
        print('VOCE PAGARA {} reais'.format(preço))
    elif quan > 2:
        juros = preço * 20 / 100
        print('VOCE PAGARA {} REAIS'.format(preço + juros))
    elif quan == 0:
        por = preço * 5 / 100
        print('VOCE PAGARA {} REAIS'.format(preço - por))

elif forma_de_pag == 2 or forma_de_pag == 3:
    por = preço * 10 / 100
    print('VOCE VAI PAGAR {} REAIS'.format(preço - por))