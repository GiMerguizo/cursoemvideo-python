print('\033[31mDesafio 056\033[m')
print('-=' * 20)
print('\033[35mAnálise de Dados\033[m')
print('-=' * 20)
import time
soma = 0
media = 0
novinhas = 0
velho = 0
anciao = ''
for pessoas in range(0, 4):
    print('--- {}ª pessoa ---'.format(pessoas+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    print('M = Masculino\nF = Feminino')
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if sexo == 'F' and idade < 20:
        novinhas += 1
    elif sexo in 'Mm':
        if idade > velho:
            velho = idade
            anciao = nome
media = soma / 4
print('\nAnalisando dados...')
time.sleep(1)
print('Média das idades = {:.2f} anos'.format(media))
print('Mulheres com menos de 20 anos: {}'.format(novinhas))
print('Homem mais velho: {}, com a idade de {} anos'.format(anciao, velho))
