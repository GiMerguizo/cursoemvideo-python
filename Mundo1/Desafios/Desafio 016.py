from math import trunc
cores = {'v1': '\033[31m', 'l': '\033[m'}
print('{}Desafio 016{}'.format(cores['v1'], cores['l']))
num = float(input('Digite um número: '))
print('O número \033[32m{}\033[m tem a parte inteira \033[36m{}\033[m'.format(num, trunc(num)))

num = float(input('Digite um número: '))
print('O número \033[32m{}\033[m tem a parte inteira \033[36m{}\033[m'.format(num, int(num)))
