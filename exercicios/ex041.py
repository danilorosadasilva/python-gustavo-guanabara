# Mostra categoria de acordo com a idade
# Ate 9 anos  : MIRIM
# Ate 14 anos : INFANTIL
# Ate 19 anos : JUNIOR
# Ate 20 anos : SENIOR
# Acima : MARTER
from datetime import date
atual = date.today().year
idd = int(input('Ano de nascimento: '))
idd = atual - idd
print(idd)
if idd <= 9:
    print('Sua categoria é MIRIM')
elif idd <= 14:
    print('Sua categoria é INFANTIL')
elif idd <= 19:
    print('Sua categoria é JUNIOR')
elif idd <= 20:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')