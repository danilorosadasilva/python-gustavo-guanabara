# nota dos alunos
boletim = []
ant_boletim = []

while True:
    Perg1 = str(input('Nome: ')).upper()
    ant_boletim.append(Perg1)

    Perg2 = float(input('Nota1: '))
    ant_boletim.append(Perg2)
    
    Perg3 = float(input('Nota2: '))
    ant_boletim.append(Perg3)

    boletim.append(ant_boletim[:])

    ant_boletim.clear()

    opç_sair = str(input('Terminar: [S/N] ')).strip().upper()[0]
    if opç_sair == 'S':
        break

print('-'*50)

for n, i in enumerate(boletim):
    print(f'{n+1}  {i[0]:<10}  |  {i[1]:<4.2f}  | {i[2]:.2f}')

print('-'*50)

while True:
    perg4 = int(input('Gostaria de saber a nota de qual aluno [digite o numero], [0 = nada]: '))
    if perg4 == 0:
        print('Obrigado. Volte sempre!!!!')
        break
    else:
        sub = perg4 - 1
        print('-'*50)
        print(f'{boletim[sub][0]:<10}  |  {boletim[sub][1]:.2f}  | {boletim[sub][2]:.2f}')
        print('-'*50)
