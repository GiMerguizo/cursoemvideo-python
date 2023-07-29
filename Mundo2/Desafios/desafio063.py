print('\033[31m Desafio 063 \033[m')
print('-=' * 20)
print('\033[35m Sequência de Fibonacci v1.0 \033[m')
print('-=' * 20)
n = int(input('Quantos elementos você deseja ver? '))
ant = 0
x = 1
cont = 3
print('{} - {}'.format(ant, x), end='')

while cont <= n:
    fn = x + ant
    print(' - {}'.format(fn), end=' ')
    ant = x
    x = fn
    cont += 1
print(' - FIM')
