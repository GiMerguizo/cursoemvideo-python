print('\033[31mDesafio 051\033[m')
print('-=' * 20)
print('\033[35mProgressão Aritmética\033[m')
print('-=' * 20)
print('O Termo Geral da P.A é: an = a1 + (n - 1)r')
print('Para calcular a P.A, digite os seguintes termos: ')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
print('Os 10 primeiros termos dessa progressão são:')
for c in range(1, 11):
    n = c
    conta = a1 + (n - 1) * r
    print(conta, end=' - ')
print('ACABOU')
# print('a{} = {}'.format(c, conta))
