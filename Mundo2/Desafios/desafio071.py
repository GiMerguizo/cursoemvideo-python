print('\033[31m Desafio 071 \033[m')
print('-=' * 20)
print('\033[35m Simulador de Caixa Eletrônico \033[m')
print('-=' * 20)

print('\nBem vind@ ao nosso Caixa Eletrônico!')
print('--' * 20)

saque = int(input('Valor do saque: R$ '))

cinco = vinte = dez = um = 0

while saque >= 50:
    cinco += 1
    saque -= 50
while saque >= 20:
    vinte += 1
    saque -= 20
while saque >= 10:
    dez += 1
    saque -= 10
while saque >= 1:
    um += 1
    saque -= 1
    
"""
cont = 0
céd = 50
total = saque
while True:
    if total >= céd:
        cont += 1
        total -= céd
    
    else:
        if cont > 0:
            print(f'{cont} cédulas de {céd}')
            cont = 0
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        else:
            break
"""

print(f'''
Cédulas sacadas:
      
{cinco} cédulas de R$ 50,00
{vinte} cédulas de R$ 20,00
{dez} cédulas de R$ 10,00
{um} cédulas de R$ 1,00

Finalizando...
''')