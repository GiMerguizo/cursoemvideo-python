print('\033[31mDesafio 031\033[m')
d = float(input('Qual é a distância da sua viagem em Km? '))
if d <= 200:
    print('O preço da viagem para \033[30;107m{} Km\033[m é de \033[32mR$ {:.2f}\033[m'.format(d, d * 0.50))
else:
    print('O preço da viagem para \033[30;107m{} Km\033[m é de \033[32mR$ {:.2f}\033[m'.format(d, d * 0.45))
""" preço = distância * 0.50 if d <= 200 else distância * 0.45
print('O preço da sua viagem será de {}'.format(preço))"""
