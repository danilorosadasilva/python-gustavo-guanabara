frase = 'Ola mundo!'
print(frase[0:8])
print(frase[:10:2]) 
print(len(frase))
print(frase.count('o'))
print(frase.find('nd'))
print('mundo' in frase)
print(frase.replace('Ola', 'Hello'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
#
frase2 = frase.split()
print('-'.join(frase2))
#
# O lower manda todas para minusculo, e o find e se a em comum,
# ja que maiusculas sao diferentes de minusculas
print(frase.lower().find('mundo'))

print("""New to contributing to Open Source Free Libre software? There is a draft of Let's write a unit test!" which is a step by step guide on how to write your first unit test in python for pygame, which is very similar to how you would do it for other projects.""")
