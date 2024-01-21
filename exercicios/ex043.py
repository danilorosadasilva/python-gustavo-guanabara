#calcular o IMC
peso = float(input('KG: '))
altura = float(input('ALTURA [M]:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 38:
    print('esta no sobrepeso')
elif 30 <= imc < 40:
    print('esta obeso')
else:
    print('mano, cê ta na merda')