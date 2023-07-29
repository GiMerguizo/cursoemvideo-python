print('\033[31mDesafio 050\033[m')
print('-=' * 20)
print('\033[35mSoma dos números pares\033[m')
print('-=' * 20)
s = 0
count = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        count += 1
print('A soma dos {} números pares digitados é \033[32m{}\033[m.'.format(count, s))
