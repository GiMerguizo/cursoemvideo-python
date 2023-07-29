from math import ceil, floor, trunc
print('-=' * 20)
print('\033[31mCálculo das médias\033[m')
print('-=' * 20)
n1 = float(input('Nota da Atividade Especial: '))
n2 = float(input('Nota da prova: '))
n3 = float(input('Nota de participação: '))
m = (n1 * 0.3 + n2 * 0.6 + n3 * 0.1)
mina = trunc(m)
if m % mina >= 0.5:
    m1 = ceil(m)
else:
    m1 = floor(m)
if m >= 8:
    print('Média final = \033[34m{:.2f}\033[m\nArredondando = \033[34m{}\033[m'.format(m, m1))
    print('\033[96mCONTINUE ASSIM!\033[m')
if 8 > m >= 5:
    print('Média final = \033[33m{:.2f}\033[m\nArredondando = \033[33m{}\033[m'.format(m, m1))
    print('\033[96mTá bom! Mas da pra melhorar.\033[m')
if m < 5:
    print('Média final = \033[31m{:.2f}\033[m\nArredondando = \033[31m{}\033[m'.format(m, m1))
    print('\033[96mEstuda menina!!\033[m')
