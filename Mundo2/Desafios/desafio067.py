print('\033[31m Desafio 067 \033[m')
print('-=' * 20)
print('\033[35m Tabuada v3.0 \033[m')
print('-=' * 20)

while True:
    n = int(input('\nQuer ver a tabuada de qual valor? '))

    if n < 0:
        break

    print('-=' * 20)
    for i in range(1, 11):
        print(f'   {n} x {i} = {n * i}')
    print('-=' * 20)

print('\nEncerrando...\n')
print('Volte sempre! \n')
