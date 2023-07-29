import random
print('\033[31mDesafio 020\033[m')
print('-=' * 20)
print('\033[35mSorteando a ordem de presentação dos trabalhos\033[m')
print('-=' * 20)
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 2: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação será ', end='')
print(lista)
