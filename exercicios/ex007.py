#desenvolver um programa que leia as duas notas de
#de um aluno e mostre a sua media.

print('_' * 35)
materia = input('qual sua materia?')
pb = float(input('Qual a nota do primeiro bimestre | '))
sb = float(input('Qual a nota do segundo bimestre | '))
tb = float(input('Qual a nota do terceiro bimestre | '))
qb = float(input('Qual a nota do quarto bimestre | '))
media = (pb + sb + tb + qb) / 4
print('A SUA MEDIA EM {} FOI DE {:.1f}'.format(materia, media))
print('_' * 35)
