# programa que pergunta a quantidade de km percorrido por um 
# carro alugado e a quantidade de dias que ele foi alugado
# calcule o tanto a pagar , sabendo que o carro custa r$60 por dia
# e r$ 0,15 por km rodado

dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km você percorreu? '))
pagar = (km * 0.15) + (dias * 60)
print('Você deve pagar: {:.2f} R$'.format(pagar))