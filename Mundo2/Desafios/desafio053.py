print('\033[31mDesafio 053\033[m')
print('-=' * 20)
print('\033[35mPALÍNDROMOS\033[m')
print('-=' * 20)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'inverso = junto[::-1]'
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}.".format(junto, inverso))
if inverso == junto:
    print('A frase é um \033[33mpalíndromo\033[m.')
else:
    print('A frase \033[91mnão\033[m é um \033[33mpalíndromo\033[m.')
