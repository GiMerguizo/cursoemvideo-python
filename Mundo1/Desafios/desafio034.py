print('\033[31mDesafio 034\033[m')
sal = float(input('Salário atual do funcionário: \033[32mR$ '))
if sal >= 1250:
    aumento = sal * 1.1
else:
    aumento = sal * 1.15
print('\033[mO salário de \033[92mR$ {:.2f}\033[m vai para \033[32mR$ {:.2f}\033[m.'.format(sal, aumento))
print('\033[33mPARABÉNS pelo aumento!!!\033[m')
