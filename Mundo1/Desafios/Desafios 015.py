from time import sleep
print('\033[31mDesafio 015\033[m')
dias = int(input('Quantos dias de aluguel? '))
print('-=' * 20)
km = float(input('Km rodados: '))
print('\033[33mProcessando...\033[m')
sleep(2)
print('O preço a pagar é de \033[32mR${:.2f}\033[m'.format(dias*60 + km*0.15))
