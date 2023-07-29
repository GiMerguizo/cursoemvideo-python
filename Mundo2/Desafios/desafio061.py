from time import sleep
print('\033[31m Desafio 061 \033[m')
print('-=' * 20)
print('\033[35m Progressão Aritmética v2.0 \033[m')
print('-=' * 20)

p1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
print('Calculando...')
sleep(1)
i = 0
while i < 10:
    print('{}'.format(p1), end=' - ')
    p1 += razao
    i += 1
print('FIM')

"""# Conta: an = a1 + (n - 1)r
i = 1
conta = 0
while i < 11:
    conta = p1 + (i - 1) * razao
    i += 1
    print('{}'.format(conta), end=' - ')
print('FIM')"""
