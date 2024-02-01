palavras = ('celular', 'computador', 'televisao', 'caderno', 'notbook', 'controle', 'teclado')
for itens in palavras:
    print(f'\nNa palavra {itens.upper()} tem : ',end='')
    for letra in itens:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')