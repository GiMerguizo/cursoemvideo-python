from math import sqrt, pow, hypot
cores = {'v1': '\033[31m', 'l': '\033[m'}
print('{}Desafio 017{}'.format(cores['v1'], cores['l']))
print('-=' * 20)
print('\033[35mCalculando a hipotenusa\033[m')
print('-=' * 20)
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)
"""hip1 = sqrt(pow(co, 2) + pow(ca, 2))
hip2 = (co ** 2 + ca ** 2) ** (1/2)"""
print('Hipotenusa = \033[33m{:.2f}\033[m'.format(hip))
