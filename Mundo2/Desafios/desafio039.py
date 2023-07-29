import datetime
print('\033[31mDesafio 039\033[m')
print('-=' * 20)
print('\033[36mAlistamento\033[m')
print('-=' * 20)
print('''Com qual gênero você se identifica:
[ 1 ] Masculino
[ 2 ] Feminino
[ 3 ] Prefiro não declarar
[ 4 ] Outro''')
sexo = int(input('Sua opção: '))
if sexo == 1:
    print('Seu alistamento é obrigatório no Brasil com 18 anos')
    ano = int(input('Em que ano você nasceu? '))
    atual = datetime.date.today().year
    idade = atual - ano
    print('Seu nascimento foi em {}, portanto fará {} ano(s)'.format(ano, idade))
    if idade < 18:
        print('Você não precisa se alistar ainda!')
        print('Falta(m) ainda {} ano(s)'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
    elif idade == 18:
        print('Já está na hora de se alistar!')
    else:
        print('Você está atrasado! Já passou da hora de alistar!')
        print('Já se passou {} ano(s)'.format(idade - 18))
        print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
elif sexo == 2:
    print('Seu alistamento não é obrigatório no Brasil.')
elif sexo == 3 or 4:
    print('''Deseja continuar com o processo de informações sobre o alistamento?
    [ 1 ] Sim
    [ 2 ] Não''')
    op = int(input('Sua opção: '))
    if op == 1:
        ano = int(input('Em que ano você nasceu? '))
        atual = datetime.date.today().year
        idade = atual - ano
        print('Seu nascimento foi em {}, portanto fará {} ano(s)'.format(ano, idade))
        if idade < 18:
            print('Você não precisa se alistar ainda!')
            print('Falta(m) ainda {} ano(s)'.format(18 - idade))
            print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
        elif idade == 18:
            print('Já está na hora de se alistar!')
        else:
            print('Você está atrasado! Já passou da hora de alistar!')
            print('Já se passou {} ano(s)'.format(idade - 18))
            print('Seu alistamento foi em {}.'.format(atual - (idade - 18)))
    if op == 2:
        print('Agradecemos pela participação!')
