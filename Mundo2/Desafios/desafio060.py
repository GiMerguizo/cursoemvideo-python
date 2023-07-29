from math import factorial
print('\033[31m Desafio 060 \033[m')
print('-=' * 20)
print('\033[35m Fatorial \033[m')
print('-=' * 20)
'''
# Modo 1
num = int(input('Digite um número: '))
n = num
fat = num
print('{} '.format(n), end='')
while num > 1:
    num -= 1
    fat = fat * num
    print('x {} '.format(num), end='')
print('= {}'.format(fat))
print('Resultado: {}! = {}'.format(n, fat))
'''
# Modo 2
num = int(input('Digite um número para calcular o fatorial: '))
f = factorial(num)
print('Resultado: {}! = {}'.format(num, f))
