from time import sleep
print('\033[31mDesafio 033\033[m')
print('-=' * 20)
print('\033[35mAchando o maior e menor número\033[m')
print('-=' * 20)
sleep(1)
print('Escolha três números aleatórios.')
n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
n3 = int(input('Terceiro: '))
if n1 > n2 > n3:
    print('O maior é o \033[34m{}\033[m e o menor é o \033[96m{}\033[m.'.format(n1, n3))
if n1 > n3 > n2:
    print('O maior é o \033[34m{}\033[m e o menor é o \033[96m{}\033[m.'.format(n1, n2))
if n2 > n3 > n1:
    print('O maior é o \033[34m{}\033[m e o menor é o \033[96m{}\033[m.'.format(n2, n1))
if n2 > n1 > n3:
    print('O maior é o \033[34m{}\033m e o menor é o \033[96m{}\033[m.'.format(n2, n3))
if n3 > n1 > n2:
    print('O maior é o \033[34m{}\033[m e o menor é o \033[96m{}\033[m.'.format(n3, n2))
if n3 > n2 > n1:
    print('O maior é o \033[34m{}\033[m e o menor é o \033[96m{}\033[m.'.format(n3, n1))
""" lista = [n1, n2, n3]
print('O maior valor digitado foi {}.'.format(max(lista)))
print('O menor valor digitado foi {}.'.format(min(lista))) """
