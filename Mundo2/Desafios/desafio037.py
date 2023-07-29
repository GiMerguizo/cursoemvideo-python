print('\033[31mDesafio 037\033[m')
print('-=' * 20)
print('\033[35mBases de Conversão\033[m')
print('-=' * 20)
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a Conversão: ')
print('\033[36m[ 1 ] \033[mBinário\n\033[36m[ 2 ]\033[m Octal\n\033[36m[ 3 ]\033[m Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('Convertendo {} para binário: \033[32m{}\033[m'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('Convertendo {} para Octal: \033[32m{}\033[m'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('Convertendo {} para Hexadecimal: \033[32m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[91mOpção inválida. Tente novamente.\033[m')
