# programa que ve a o ano q ele nasceu :
# se ele  ainda vai se alistar ao serviço militar
# se e hora de se alistar
# se ja passou o tempo de se alistar 
# deve tambem mostrar o tempo que falta ou passou

from datetime import date
idd = int(input('Em que ano você nasceu: '))
# Extraindo o ano atual
ano_atual = date.today().year
# Tirado do bing
idd = ano_atual - idd
if idd < 18:
    print('\033[32mFalta {} anos para voce se alistar.\033[m'.format(18 - idd))
elif idd > 18:
    print('\033[32mJa passou passou {} anos da sua idade de se alistar.\033[m'.format(idd - 18))
else:
    print('\033[0;31mVai ter que se alistar!!!!!!!!!Seu fudeu kkkkkkkkkkkkkkk\033[m')