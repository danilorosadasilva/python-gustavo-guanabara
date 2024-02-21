per = str(input('Digite a espressão: '))

pilha = []

for i in per:
    if i == '(':
        pilha.append('(')
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('A espressao esta errada.')
else:
    print('A espressao esta certa.')