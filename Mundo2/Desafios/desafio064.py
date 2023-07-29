print('\033[31m Desafio 064 \033[m')
print('-=' * 20)
print('\033[35m Tratando vários valores \033[m')
print('-=' * 20)

num = cont = soma = 0

print('--' * 30)
print('Digite quantos números quiser!')
print('Para encerrar o programa, digite o número "999".')
print('--' * 30)
while num != 999:
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
print('\nForam digitados {} números.'.format(cont - 1))
print('Soma dos números digitados: {}'.format(soma - 999))
