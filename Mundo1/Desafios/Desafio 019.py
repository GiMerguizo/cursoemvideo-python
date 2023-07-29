import random
print('\033[31mDesafio 019\033[m')
print('Nome dos alunos a serem sorteados: ')
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
print('O aluno sorteado foi \033[4m{}'.format(random.choice(lista)))
