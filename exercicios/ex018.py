#calcular o ceno e cosseno
from math import sin, radians, cos, tan
ângulo = float(input('digite o angulo que voce deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem seno de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O angulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))