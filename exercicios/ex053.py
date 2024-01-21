frase = str(input('digite: ')).strip().upper()
palvras = frase.split()
junto = ''.join(palvras)
inverso = junto[::-1]
if inverso == junto:
    print('E um palindromo')
else:
    print('nao e um palindromo')