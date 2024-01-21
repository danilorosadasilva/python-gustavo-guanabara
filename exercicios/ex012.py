#algotimo de tirar 5% do produto

produto = float(input('qual o preço do produto?  R$'))
desconto = produto - (produto / 100 * 5)
print('O novo preço do produto será {:.2f} reais.'.format(desconto))