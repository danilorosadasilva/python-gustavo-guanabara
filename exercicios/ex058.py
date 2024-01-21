import random 
sorteio = random.randint(1,10)

jogador = 11
count_jog = 0
print('{:-^80}'.format('Tente-adivinhar-qual-o-numero-que-o-computador-jogou-de-1-á-10'))
print('')
while jogador != sorteio:
    jogador = int(input('Numero: '))
    if jogador != sorteio:
        print('Tente novamente....')
    count_jog += 1

if count_jog <= 2:
    print('\033[32mVoce conceguiu acertar o numero {}, PARABENS, com apenas {} tentativas.\033[m'.format(sorteio, count_jog))
elif count_jog <= 4:
    print('\033[32mMuito bom, apenas {} tentativas.\033[m'.format(count_jog))
else:
    print('\033[31mVoce foi orrivel, {} tentativas\033[m'.format(count_jog))
