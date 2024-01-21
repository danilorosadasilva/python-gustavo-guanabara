#desafio 003
#verificar o tipo do digitado

a = input('digite augo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('E um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('esta em maiusculas?', a.isupper())
print('esta em minusculas?', a.islower())
#capitalizada é maiusculas e minusculas
print('esta capitalizada?', a.istitle())