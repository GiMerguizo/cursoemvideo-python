print('\033[31mDesafio 029\033[m')
vel = float(input('Velocidade que estava o carro: '))
if vel <= 80:
    print('\033[92mO carro passou dentro do limite de velocidade (80 Km/h).\033[m')
else:
    print('\033[31mMULTADO!\033[m O carro ultrapassou o limite de velocidade (80 Km/h).')
    print('\033[33mA multa será de R$ {:.2f}.\033[m'.format((vel - 80) * 7))
print('\033[96mTenha um bom bia! Dirija com segurança!\033[m')
