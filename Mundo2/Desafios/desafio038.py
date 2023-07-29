print('\033[31mDesafio 038\033[m')
print('-=' * 20)
print('\033[36m-- Escolha dois números --\033[m')
p = int(input('Primeiro: '))
s = int(input('Segundo: '))
if p > s:
    print('{} é maior que {} => {} > {}'.format(p, s, p, s))
elif s > p:
    print('{} é maior que {} => {} > {}'.format(s, p, s, p))
elif p == s:
    print('Não existe valor maior, os dois são iguais => {} = {}'.format(p, s))
'''else:
    print('Os dois números são iguais => {} = {}'.format(p, s))'''
