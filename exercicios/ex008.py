#Conver ter um vados de metros em centimetros
#e milimetros

m = float(input("quantos metros?"))
cen = m * 100
min = m * 1000
print('*{}* metros dá *{:.0f}* centimetros e *{:.0f}* milimetros'.format(m, cen, min))
