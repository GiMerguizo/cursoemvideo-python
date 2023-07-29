cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'magenta': '\033[35m', 'ciano': '\033[36m', 'cinza': '\033[37m'}
"""print('\033[31mDesafio 009\033[m')
print('-=' * 20)
print('\033[33mTabuada\033[m')
print('-=' * 20)
n1 = int(input('Quero a tabuada de: '))
print('{}x1 = \033[35m{}\033[m'.format(n1, n1*1))
print('{}x2 = \033[35m{}\033[m'.format(n1, n1*2))
print('{}x3 = \033[35m{}\033[m'.format(n1, n1*3))
print('{}x4 = \033[35m{}\033[m'.format(n1, n1*4))
print('{}x5 = \033[35m{}\033[m'.format(n1, n1*5))
print('{}x6 = \033[35m{}\033[m'.format(n1, n1*6))
print('{}x7 = \033[35m{}\033[m'.format(n1, n1*7))
print('{}x8 = \033[35m{}\033[m'.format(n1, n1*8))
print('{}x9 = \033[35m{}\033[m'.format(n1, n1*9))
print('{}x10 = \033[35m{}\033[m'.format(n1, n1*10))

print('\033[31mDesafio 010\033[m')
r = float(input('Quanto você quer converter para dólar? \033[32mR$'))
d = r/5.56
print('\033[mCom \033[31m{} reais\033[m, você pode comprar \033[36m{:.2f} dólares\033[m.'.format(r, d))

print('{}Desafio 011{}'.format(cores['vermelho'], cores['limpa']))
ml = float(input('\033[34mLargura\033[m da parede: '))
a = float(input('\033[33mAltura\033[m da parede: '))
print('A área da parede é {}{} m²{}'.format(cores['ciano'], ml*a, cores['limpa']))
print('Você precisará de \033[32m{} litros\033[m de tinta para pintar essa parede ({}x{}).'.format(ml*a*(1/2), ml, a))

print('{}Desafio 012{}'.format(cores['vermelho'], cores['limpa']))
p1 = float(input('Preço do produto: R$'))
print('Com \033[32m5% de desconto\033[m, o produto vale \033[34mR${:.2f}\033[m'.format(p1*0.95))

print('{}Desafio 013{}'.format(cores['vermelho'], cores['limpa']))
s = float(input('Salário: R$'))
print('O novo salário com \033[32m15% de aumento\033[m é \033[35mR${:.2f}\033[m'.format(s*1.15))"""

print('{}Desafio 014{}'.format(cores['vermelho'], cores['limpa']))
print('-=' * 20)
print('{}Conversão de temperaturas{}'.format(cores['magenta'], cores['limpa']))
print('-=' * 20)
print('{}Celsius --> Farenheit e Kelvin\033[m'.format(cores['verde']))
c = float(input('Temperatura em {}ºC\033[m: '.format(cores['amarelo'])))
f = 9 * c / 5 + 32
k = c - 273
print('\033[33m{} ºC{} é igual a \033[34m{:.2f} ºF\033[m e \033[35m{:.2f} K\033[m'.format(c, cores['limpa'], f, k))

print('{}Farenheit --> Celsius e Kelvin\033[m'.format(cores['verde']))
f1 = float(input('Temperatura em {}ºF{}: '.format(cores['azul'], cores['limpa'])))
c1 = (f1 * 5 - 160)/9
k1 = c1 + 273
print('\033[34m{} ºF\033[m é igual a \033[33m{:.2f} ºC\033[m e \033[35m{:.2f} K\033[m'.format(f1, c1, k1))

print('{}Kelvin --> Celsius e Farenheit{}'.format(cores['verde'], cores['limpa']))
k2 = float(input('Temperatura em \033[35mK\033[m: '))
c2 = k2 + 273
f2 = 9 * ((k2 - 273)/5) + 32
print('\033[35m{} K\033[m é igual a \033[33m{:.2f} ºC\033[m e \033[34m{:.2f} ºF\033[m'.format(k2, c2, f2))

print('{}Concluindo:{}'.format(cores['vermelho'], cores['limpa']))
print('{} ºC = {:.2f} ºF = {:.2f} K\n{} ºF = {:.2f} ºC = {:.2f} K'.format(c, f, k, f1, c1, k1))
print('{} K = {:.2f} ºC = {:.2f} ºF'.format(k2, c2, f2))
