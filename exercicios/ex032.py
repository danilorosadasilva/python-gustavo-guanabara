#ver se o ano é bissesto
from datetime import date
ano = int(input('Digite o ano (coloque 0 para analizar o ano atual) : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano BISSESTO'.format(ano))
else:
    print('{} não é um ano BISSESTO'.format(ano))