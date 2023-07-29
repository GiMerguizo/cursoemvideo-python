from datetime import date
print('\033[31mDesafio 054\033[m')
print('-=' * 20)
print('\033[35mGrupo da Maioridade\033[m')
print('-=' * 20)
sist = date.today().year
count1 = 0
count2 = 0
idade = 0
print('Ano atual: {}'.format(sist))
for c in range(0, 7):
    ano = int(input('{}º ano de nascimento: '.format(c+1)))
    idade = sist - ano
    if idade >= 21:
        count1 += 1
    elif idade < 21:
        count2 += 1
print('\033[96m{}\033[m pessoas já atingiram a maioridade.'.format(count1))
print('\033[96m{}\033[m pessoas ainda não atingiram a maioridade.'.format(count2))
