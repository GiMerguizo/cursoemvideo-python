print('\033[31m Desafio 065 \033[m')
print('-=' * 20)
print('\033[35m Vários números com flag \033[m')
print('-=' * 20)

print('Digite 999 para encerrar o programa.\n')

cont = soma = 0
while True:
    num = int(input('Digite um número: '))

    if num == 999:
        print('Encerrando...\n')
        break

    cont += 1
    soma += num

print(f'Números digitados: {cont}\nSoma: {soma}')
