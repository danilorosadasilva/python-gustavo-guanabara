t1 = int(input('primeiro termo: '))
rasao = int(input('rasao:'))
desimo= t1 + (10 - 1) * rasao
for c in range(t1, desimo + rasao, rasao):
    print('{} '.format(c), end=' => ')
print('acabou')