print('\033[31m Desafio 069 \033[m')
print('-=' * 20)
print('\033[35m Análise de dados do grupo \033[m')
print('-=' * 20)

maiorIdade = homem = mulher = 0
while True:  
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))

    if idade >= 18:
        maiorIdade += 1

    sexo = str(input('Gênero [F/M]: ')).strip()[0]
    while sexo not in 'FfMm':
        sexo = str(input('Gênero [F/M]: ')).strip()[0]

    if sexo in 'Mm':
        homem += 1
    else:
        if idade < 20:
            mulher += 1

    op = str(input('Deseja continuar [S/N]? ')).strip()[0]

    while op not in 'SsNn':
        print('Opção Inválida! Tente novamente!')
        op = str(input('Deseja continuar [S/N]? ')).strip()[0]
    
    if op in 'Nn':
        print('\nFinalizando...\n')
        break
    
    print('\n')

print('--' * 20)    
print(f'Maiores de 18 anos: {maiorIdade}')
print(f'Homens: {homem}')
print(f'Mulheres com menos de 20 anos: {mulher}')
print('--' * 20)
print('\n')
