print('\033[31m Desafio 059 \033[m')
print('-=' * 20)
print('\033[35m Menu \033[m')
print('-=' * 20)
opcao = 0
print('Digite dois números.')
num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
while opcao != 5:
    print('--' * 20)
    print('Escolha uma operação...')
    print('[1] Soma\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('Opção: '))
    print('--' * 20)
    if opcao == 1:
        print('Opção escolhida: SOMA')
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
        print('Resultado: {}'.format(num1 + num2))
    elif opcao == 2:
        print('Opção escolhida: MULTIPLICAÇÃO')
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
        print('Resultado: {}'.format(num1 * num2))
    elif opcao == 3:
        print('Opção escolhida: MAIOR')
        if num1 > num2:
            print('{} > {}'.format(num1, num2))
            print('Maior: {}'.format(num1))
        elif num1 < num2:
            print('{} > {}'.format(num2, num1))
            print('Maior: {}'.format(num2))
        else:
            print('Os dois números são iguais.\n{} = {}'.format(num1, num2))
    elif opcao == 4:
        print('Opção escolhida: NOVOS NÚMEROS')
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))
    elif opcao == 5:
        print('Finalizando programa...')
    else:
        print('Algo deu errado! Tente novamente!')

