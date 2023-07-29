from time import sleep
print('\033[31mDesafio 025\033[m')
nome = str(input('Qual é o seu nome completo? ')).strip()
print('\033[35mVerificando se seu nome possui Silva...\033[m ', end='>>>>>>>>>> ')
sleep(2)
nome = nome.upper()
print('SILVA' in nome)
