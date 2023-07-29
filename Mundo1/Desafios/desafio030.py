print('\033[31mDesafio 030\033[m')
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('\033[33m{} é par.\033[m'.format(num))
else:
    print('\033[34m{} é ímpar.\033[m'.format(num))
