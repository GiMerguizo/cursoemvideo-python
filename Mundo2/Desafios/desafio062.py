from time import sleep
print('\033[31m Desafio 062 \033[m')
print('-=' * 20)
print('\033[35m Super Progressão Aritmética v3.0 \033[m')
print('-=' * 20)

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
i = 0
termo = 'S'
cont = 10
print('Calculando...')
sleep(1)
while i < 10:
    print('{}'.format(p1), end=' - ')
    p1 += razao
    i += 1
print('PAUSA\n')
while termo != 'N':
    termo = str(input('Quer ver mais algum termo? [S/N] ')).upper()
    if termo == 'N':
        print('Encerrando programa...')
        sleep(1)
    elif termo == 'S':
        qtde = int(input('Quantos? '))
        cont += qtde
        if qtde == 0:
            print('Encerrando programa...')
            termo = 'N'
            sleep(1)
        else:
            i = 0
            while i < qtde:
                print('{}'.format(p1), end=' - ')
                p1 += razao
                i += 1
            print('FIM')
sleep(1)
print('Programa finalizado com {} termos mostrados.'.format(cont))
