n = 0
while n >= 0:
    n = int(input('qual tabuada vc quer: '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n * i}')
print('fim')