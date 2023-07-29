from datetime import date
print('\033[31mDesafio 041\033[m')
print('-=' * 20)
print('\033[35m Categorias de Natação \033[m')
print('-=' * 20)
ano = int(input('Ano de nascimento do atleta: '))
sist = date.today().year
idade = sist - ano
print('Para {} anos:'.format(idade))
if idade <= 9:
    print('Categoria: \033[96mMirim\033[m')
elif 9 < idade <= 14:
    print('Categoria: \033[96mInfantil\033[m')
elif 14 < idade <= 19:
    print('Categoria: \033[96mJunior\033[m')
elif 19 < idade <= 25:
    print('Categoria: \033[96mSênior\033[m')
elif idade > 25:
    print('Categoria: \033[96mMaster\033[m')
print('\033[33mBoa natação!\033[m')
