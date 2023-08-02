from random import randint
from time import sleep
result = ''
cont = 0
while True:
    num = int(input('Seu número: '))
    op = str(input('PAR OU ÍMPAR [P/I]? ')).strip()[0].upper()
    pc = randint(0, 10)
    soma = num + pc

    if soma % 2 == 0:
        result = 'PAR'
    else:
        result = 'IMPAR'
    print(f'Você jogou {num} e o computador jogou {pc}. \nTOTAL: {soma} - {result}')
    print('--' * 20)
    sleep(2)
    
    if op == result.strip()[0]:
        print('\nVocê ganhou!\nVamos jogar novamente!\n')
        print('--' * 20)
        cont += 1
    else:
        print(f'Você perdeu!\nGAME OVER! Você ganhou por {cont} vezes consecutivas.')
        print('\nFinalizando...')
        break
