from time import sleep
cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'magenta': '\033[35m', 'ciano': '\033[36m', 'cinza': '\033[37m'}
print('{}Desafio 003{}'.format(cores['vermelho'], cores['limpa']))
print('-=' * 20)
print('\033[33mFazendo soma\033[m')
print('-=' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('{}{}{} + {}{}{} = {}{}{}'.format(cores['azul'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'],
                                        cores['verde'], s, cores['limpa']))
sleep(2)
print('\033[31mDesafio 004\033[m')
print('-=' * 20)
print('\033[33mAnalisando o termo\033[m')
print('-=' * 20)
x = input('Digite algo: ')
print('O tipo primitivo desse valor é\033[34m', type(x))
print('\033[mEstá capitalizado?\033[34m', x.istitle())
print('\033[mÉ alfanúmerico?\033[34m', x.isalnum())
print('\033[mÉ alfabético?\033[34m', x.isalpha())
print('\033[mÉ um decimal?\033[34m', x.isdecimal())
print('\033[mÉ um número?\033[34m', x.isnumeric())
print('\033[mEstá todo em maiúsculo?\033[34m', x.isupper())
print('\033[mEstá todo em minúsculo?\033[34m', x.islower())
print('\033[mSó tem espaços?\033[34m', x.isspace())
sleep(3)
print('\033[31mDesafio 005\033[m')
print('-=' * 20)
print('\033[33mAntecessor e sucessor\033[m')
print('-=' * 20)
n1 = int(input('Escolha um número: '))
a = n1 - 1
s = n1 + 1
print('Seu {}antecessor{} é \033[4m{}\033[m e seu {}sucessor{} é \033[4m{}\033[m.'.format(cores['magenta'],
                                                                                          cores['limpa'], a,
                                                                                          cores['amarelo'],
                                                                                          cores['limpa'], s))
sleep(2)
print('\033[31mDesafio 006\033[m')
print('-=' * 20)
print('\033[33mMultiplicando\033[m')
print('-=' * 20)
n2 = int(input('Escolha um número: '))
d = n2 * 2
t = n2 * 3
r = n2 ** (1/2)
print("""O \033[1mdobro\033[m é {}{}{}, o \033[1mtriplo\033[m é {}{}{} e a \033[1mraiz quadrada\033[m é 
{}{:.2f}{}.""".format(cores['vermelho'], d, cores['limpa'], cores['azul'], t, cores['limpa'], cores['verde'], r,
                      cores['limpa']))
sleep(3)
print('\033[31mDesafio 007\033[m')
print('-=' * 20)
print('\033[33mMédia\033[m')
print('-=' * 20)
n3 = float(input('Primeira nota: '))
n4 = float(input('Segunda nota: '))
m = (n3 + n4)/2
if m >= 5:
    cor = '\033[34m'
else:
    cor = '\033[31m'
print('Sua média é {}{}\033[m'.format(cor, int(m)))
sleep(3)
print('\033[31mDesafio 008\033[m')
print('-=' * 20)
print('Conversões')
print('-=' * 20)
m1 = float(input('Para começar a conversão digite um valor em metros: '))
km = m1/1000
hm = m1/100
dam = m1/10
metros = m1
dm = m1*10
cm = m1*100
mm = m1*1000
print('\033[36mSeu valor vale:\033[m {} Km, {} hm, {} dam, {} m, {} dm, {} cm, {} mm'.format(km, hm, dam, metros, dm,
                                                                                             cm, mm))
