print('\033[31mDesafio 027\033[m')
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Primeiro nome: \033[37m{:-<20}\033[m'.format(n[0]))
print('último nome: \033[90m{:->20}\033[m'.format(n[len(n)-1]))