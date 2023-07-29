from datetime import date
print('\033[31mDesafio 032\033[m')
ano = int(input('Que ano você quer analisar? \033[97mColoque \033[4m0\033[m \033[97mpara analisar o ano atual:\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[92mO ano \033[7m{}\033[m \033[92mé bissexto.\033[m'.format(ano))
else:
    print('\033[91mO ano \033[7m{}\033[m \033[91mnão é bissexto.\033[m'.format(ano))
