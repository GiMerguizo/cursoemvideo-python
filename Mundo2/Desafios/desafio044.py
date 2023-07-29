print('\033[31m Desafio 044 \033[m')
print('-=' * 20)
print('\033[35mPagamento\033[m')
print('-=' * 20)
p = float(input('Peço normal (sem desconto): R$ '))
print('Forma de pagamento (dinheiro, cheque ou cartão): ')
print('''[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais nos cartão''')
op = int(input('Sua opção: '))
dez = p * 0.9
if op == 1:
    print('À vista com 10% desconto: R${:.2f}'.format(dez))
elif op == 2:
    print('À vista no cartão o produto recebe 5% de desconto.')
    print('Preço final = R${:.2f}'.format(p * 0.95))
elif op == 3:
    print('Em até 2x no cartão, o preço é o mesmo.')
    print('Preço final = {:.2f}'.format(p))
elif op == 4:
    print('3x ou mais no cartão, há 20% de juros.')
    print('Preço final = R$ {:.2f}'.format(1.2 * p))
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')
