import math

angulo = float(input('Digite o ângulo que você deseja: '))
radAng = math.radians(angulo)
sen = math.sin(radAng)
cos = math.cos(radAng)
tg = math.tan(radAng)

print('O ângulo de {0:0.1f} tem o SENO de {1:0.2f}'.format(angulo, sen))
print('O ângulo de {0:0.1f} tem o COSSENO de {1:0.2f}'.format(angulo, cos))
print('O ângulo de {0:0.1f} tem a TANGENTE de {1:0.2f}'.format(angulo, tg))
