# LER frase e ver se tem: Quantidade de A
# Posiçao que ela aparece a primeira vez
# Posiçao que ela aparece a ultima vez

fra = str(input('Incira uma frase => ')).upper().strip()
print('---- A letra a apareceu {} veses na frase.'.format(fra.count('A')))
print('---- A primeira letra _A_ apareceu na posição => {}'.format(fra.find('A')+1))
print('---- A última letra _A_ apareceu na posição   => {}'.format(fra.rfind('A')+1))
