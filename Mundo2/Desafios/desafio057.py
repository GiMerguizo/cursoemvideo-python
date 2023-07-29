print('\033[31mDesafio 057\033[m')
print('-=' * 20)
print('\033[35mValidação de Dados\033[m')
print('-=' * 20)

sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Algo deu errado! Tente novamente!')
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
print('Sexo: {}'.format(sexo))
