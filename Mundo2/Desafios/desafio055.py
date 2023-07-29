print('\033[31mDesafio 055\033[m')
print('-=' * 20)
print('\033[35mMaior e menor da sequência\033[m')
print('-=' * 20)
print('\033[1m*Obs.: peso em kg\033[m')
maior = 0
menor = 0
for i in range(0, 5):
    peso = float(input('{}º peso: '.format(i+1)))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Menor peso digitado: {:.2f}kg'.format(menor))
print('Maior peso digitado: {:.2f}kg'.format(maior))
