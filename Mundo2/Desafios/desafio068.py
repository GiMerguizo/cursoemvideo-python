print('\033[31m Desafio 068 \033[m')
print('-=' * 20)
print('\033[35m Jogo do Par ou Ímpar \033[m')
print('-=' * 20)

from random import randint
from time import sleep
result = ''
cont = 0
while True:
    num = int(input('Seu número: '))
    pc = randint(0, 10)
    soma = num + pc

    op = ' '
    while op not in 'PI':
        op = str(input('PAR OU ÍMPAR [P/I]? ')).strip()[0].upper()

    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'

    print(f'Você jogou {num} e o computador jogou {pc}. \nTOTAL: {soma} - DEU {result}')
    print('--' * 20)
    sleep(2)
    
    if op == result.strip()[0]:
        print('\nVocê ganhou!\nVamos jogar novamente!\n')
        print('--' * 20)
        cont += 1
    else:
        print(f'Você perdeu!\n\nGAME OVER! Você ganhou por {cont} vezes consecutivas.')
        print('\nFinalizando...\n')
        break
