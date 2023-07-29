print('\033[31m Desafio 043 \033[m')
print('-=' * 20)
print('\033[35m Calculando o IMC \033[m')
print('-=' * 20)
peso = float(input('Peso (em kg): '))
alt = float(input('Altura (em metros): '))
imc = peso / (alt ** 2)
print('Seu IMC é \033[33m{:.1f}\033[m'.format(imc))
print('\033[32mSeu status:\033[m')
if imc < 16:
    print('\033[96mMagreza grau III\033[m')
elif 16 <= imc < 17:
    print('\033[96mMagreza grau II\033[m')
elif 17 <= imc < 18.5:
    print('\033[96mMagreza grau I\033[m')
elif 18.5 <= imc < 25:
    print('\033[96mAdequado\033[m')
elif 25 <= imc < 30:
    print('\033[96mPré-obeso\033[m')
elif 30 <= imc < 35:
    print('\033[96mObesidade grau I')
elif 35 <= imc < 40:
    print('\033[96mObesidade grau II')
elif imc >= 40:
    print('\033[96mObesidade grau III\033[m')
