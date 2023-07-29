print('\033[31mDesafio 035\033[m')
print('-=' * 20)
print('\033[35mAnalisador de Triângulos\033[m')
print('-=' * 20)
c1 = float(input('Comprimento da primeira reta: '))
c2 = float(input('Comprimento da segunda reta: '))
c3 = float(input('Comprimento da terceira reta: '))
if c1 < c2 + c3 and c2 < c1 + c3 and c3 < c1 + c2:
    print('Essas três retas, de medidas {:.2f}, {:.2f} e {:.2f}, \033[32mpodem formar um triângulo.\033[m'.format(c1, c2, c3))
else:
    print('Essas três retas \033[91mnão\033[m podem formar um triângulo.')
