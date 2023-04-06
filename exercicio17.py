from math import hypot

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

# hi = (co ** 2 + ca ** 2) ** (1/2)
hi = hypot(co, ca)
print('Hipotenusa: {0:0.2f}'.format(hi))
