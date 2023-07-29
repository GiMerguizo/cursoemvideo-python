print('\033[31mDesafio 052\033[m')
print('-=' * 20)
print('\033[35mNÚMEROS PRIMOS\033[m')
print('-=' * 20)
n = int(input('Digite um número: '))
"""mult = 0
for c in range(2, n):
    divisao = n % c
    if divisao == 0:
        print('Múltiplo de', c)
        mult += 1
if mult == 0:
    print('{} é primo.'.format(n))
else:
    print('{} não é primo.'.format(n))"""
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
print('\n\033[m O número {} foi dividido {} vezes.'.format(n, tot))
if tot == 2:
    print('Por isso, {} É PRIMO!'.format(n))
else:
    print('Por isso, {} \033[91mNÃO\033[m É PRIMO!'.format(n))
