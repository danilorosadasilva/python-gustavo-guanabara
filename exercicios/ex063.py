n = int(input('Quantos termos da sequencia de fibonati? '))
count = 0
n1 = 0
n2 = 1
n3 = 0
print('{} => {}'.format(n1, n2), end='')
while n != count:
    n3 = n1 + n2
    print(' => {}'.format(n3),end='')
    n1 = n2
    n2 = n3
    count += 1