print('\033[31mDesafio 036\033[m')
print('-=' * 20)
print('\033[35mAprovando Empréstimo\033[m')
print('-=' * 20)
valor = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos quer pagar a casa? '))
mensal = valor / (12 * anos)
print('O valor da prestação mensal será de R${:.2f}'.format(mensal))
if mensal >= 0.3 * sal:
    print('Sinto muito, sua casa não pode ser financiada nesse valor, pois passou de 30% do salário.')
else:
    print('Sua casa pode ser financiada!')
