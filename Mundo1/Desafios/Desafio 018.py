import math
cores = {'v1': '\033[31m', 'l': '\033[m', 'm': '\033[35m'}
print('{}Desafio 018{}'.format(cores['v1'], cores['l']))
print('-=' * 20)
print('{}Valor do seno, cosseno e tangente{}'.format(cores['m'], cores['l']))
print('-=' * 20)
x = float(input('Valor do ângulo: '))
rad = math.radians(x)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('sen {} = \033[33m{:.2f}\033[m\ncos {} = \033[32m{:.2f}\033[m\ntg {} = \033[34m{:.2f}\033[m'.format(x, sen, x,
                                                                                                          cos, x, tan))
