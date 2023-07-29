import time
print('\033[31mDesafio 026\033[m')
frase = str(input('Digite uma frase: ')).strip().upper()
print('\033[35mAnalisando frase...\033[m')
time.sleep(2)
print('A \033[97mletra A\033[m aparece \033[36m{} vezes\033[m.'.format(frase.count('A')))
print('O \033[97mprimeiro A\033[m aparece na \033[36mposição {}\033[m.'.format(frase.find('A')+1))
print('O \033[97múltimo A\033[m aparece na \033[36mposição {}\033[m.'.format(frase.rfind('A')+1))
