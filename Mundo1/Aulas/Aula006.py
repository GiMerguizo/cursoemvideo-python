# n1 = input('Digite algo: ')
# print(type(n1))
# n2 = int(input('Digite um número: '))
# print(type(n2))
# n3 = int(input('Digite outro: '))
# s = n2 + n3
# print('A soma entre {} e {}, vale {}'.format(n2, n3, s))
# print('A soma entre', n2, 'e', n3, ',vale', s)
# n = float(input('Digite um valor: '))
# print(n)
# print(n1.isnumeric())
# print(n1.isprintable())
#
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
p = n1 ** n2
print('A soma é {}, a subtração é {} e a multiplicação é {}.'.format(s, sub, m), end=' >>> ')
print('A divisão é {:.3f}, a divisão inteira é {}, o resto é {} e a potenciação é {}.'.format(d, di, r, p))
