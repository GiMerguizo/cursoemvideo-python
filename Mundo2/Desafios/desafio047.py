print('\033[31mDesafio 047\033[m')
print('-=' * 20)
print('\033[35mNúmeros pares\033[m')
print('-=' * 20)
print('Todos os números pares entre 1 e 50 são: ')
for c in range(0, 51, 2):
    """print('.', end=' ')"""
    if c != 0:
        print(c, end=' ')
