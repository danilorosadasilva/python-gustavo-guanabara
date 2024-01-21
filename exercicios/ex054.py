pessoas = 0
for i in range(1,8):
    idade = int(input('Qual a idade da pessoa {} : '.format(i)))
    if idade >= 21:
        pessoas += 1
print('{} pessoas ja sao maior de idade e {} ainda nao'
      .format(pessoas, 7 - pessoas))