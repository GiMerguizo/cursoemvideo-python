print('\033[31mDesafio 040\033[m')
print('-=' * 20)
print('\033[35mCalculando a Média\033[m')
print('-=' * 20)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[31mREPROVADO! \033[mSua média foi \033[1m{:.1f}\033[m.'.format(m))
    print('\033[36mEstude mais! Você consegue!\033[m')
elif 5 <= m < 7:
    print('\033[33mRECUPERAÇÃO!\033[m Sua média foi \033[1m{:.1f}\033[m.'.format(m))
    print('\033[36mEstude mais! Você consegue!\033[m')
elif m >= 7:
    print('\033[32mAPROVADO!\033[m Sua média foi \033[1m{:.1f}\033[m.'.format(m))
    print('\033[36mParabéns! Continue assim!\033[m')
