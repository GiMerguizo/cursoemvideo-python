print('\033[7;40mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
nome = 'Giovaninha'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'pretoebranco': '\033[7;40'}
print('Olá, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))
