print('\033[31m Desafio 065 \033[m')
print('-=' * 20)
print('\033[35m Maior e Menor valores \033[m')
print('-=' * 20)

op = 'S'
soma = cont = maior = menor = 0
while op in 'Ss':
    num = int(input('Digite um número: '))
    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    cont += 1
    soma += num
    # while op != 'S' or op != 'N':
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma/cont
print('--' * 20)
print(f'Você digitou {cont} números.')
print('Média: {:.2f}'.format(media))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
