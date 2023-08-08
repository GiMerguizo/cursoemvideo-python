print('\033[31m Desafio 070 \033[m')
print('-=' * 20)
print('\033[35m {:^36} \033[m'.format('Estatísticas em produtos'))
print('-=' * 20)

total = mil = 0
cont = 1

while True:
    print('\n')
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco

    if preco > 1000:
        mil += 1
    
    if cont == 1 or preco < menorPreco:
        nomeBarato = nome
        menorPreco = preco
        cont = 0
    
    op = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]

    while op not in 'SN':
        print('Opção Inválida! Tente novamente!')
        op = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    
    if op == 'N':
        print('\nFinalizando...\n')
        break

print('--' * 20)
print(f'Total da compra: R$ {total:.2f}')
print(f'Produtos que custam mais que R$ 1000.00: {mil}')
print(f'Produto mais barato: {nomeBarato} - que custou R$ {menorPreco:.2f}')
print('--' * 20)