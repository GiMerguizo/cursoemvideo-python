from time import sleep
print('\033[31mDesafio 042\033[m')
print('-=' * 20)
print('\033[35m Desafio dos Triângulos \033[m')
print('-=' * 20)
print('Coloque as medidas')
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas, de medidas {}, {}, {}, \033[32mpodem formar um triângulo\033[m.'.format(r1, r2, r3))
    sleep(1)
    if r1 == r2 == r3:
        print('O triângulo formado é \033[96mEQUILÁTERO\033[m, ou seja, com todas as medidas iguais ({}).'.format(r1))
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('O triângulo formado é \033[96mISÓSCELES\033[m, ou seja, com duas medidas iguais.')
    elif r1 != r2 != r3:
        print('O triângulo formado é \033[96mESCALENO\033[m, ou seja, com todas as medidas diferentes.')
else:
    print('Essas retas, com medidas {}, {}, {}, \033[91mnão formam triângulo\033[m.'.format(r1, r2, r3))
