import random
count = 0
while True:
    computador = random.randint(1,50)
    print(f'{'PAR OU INPAR':-^30}')

    jog =   int(input('Numero: '))
    tip =   str(input('Impar ou par[I/P]: ')).strip().upper()
    resut = computador + jog


    if tip == 'I' and resut % 2 == 1:
        print('Voce ganhou. Muito bom!!!!!')
        count += 1
    elif tip == 'P' and resut % 2 == 0:
        print('Voce ganhou. Muito bom!!!!!')
        count += 1
    else:
        break
print(f'\033[32mVoce ganhou com {count} tentativas\033[m')



    