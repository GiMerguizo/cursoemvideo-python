print('\033[31mDesafio 048\033[m')
print('-=' * 20)
print('\033[35mSoma de ímpares e múltiplos de três\033[m')
print('-=' * 20)
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont = cont + 1
print('A soma dos {} valores solicitados é {}.'.format(cont, s))
print('Resultado: {}'.format(s))
