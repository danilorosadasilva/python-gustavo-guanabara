# FASER UM PROGRAMA QUE :
# <> LEIA A VELOCIDADE DE UM CARRO;
# <> SE ULTRAPASSAR 80KM/H, MOSTRAR MENSAGEM DIZENDO QUE FOI MULTADO;
# <> A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.

ve = float(input('QUAL A VELOCIDADE DO CARRO => '))
if ve > 80:
    print('Você foi multado!!')
    print('Sua multa é de R$ => {:.2f} reais'.format((ve - 80) * 7))
print('Tenha um bom dia, dirija com segurança')
print('{:-^40}'.format('fim do programa'))