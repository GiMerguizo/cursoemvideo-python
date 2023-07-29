from time import sleep
print('\033[31mDesafio 023\033[m')
num = int(input('Digite um número entre \033[96m0 e 9999:\033[m '))
# un = num % 10
# num1 = num - un
# dezena = int((num1 / 10) % 10)
# centena = int((((num1 / 10) - dezena) / 10) % 10)
# milhar = int((((num1 / 10) - dezena) / 10) / 10)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: \033[93m{}\033[m'.format(u))
print('Dezena: \033[93m{}\033[m'.format(d))
print('Centena: \033[93m{}\033[m'.format(c))
print('Milhar: \033[93m{}\033[m'.format(m))
#
n = str(num)   # SÓ é possível com algarismo de 4 dígitos
print('\033[35mAnalisando o número \033[4;35m{}\033[m ...\033[m'.format(num))
sleep(2)
print('\033[94mUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}\033[m'.format(n[3], n[2], n[1], n[0]))
