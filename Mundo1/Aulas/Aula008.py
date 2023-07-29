import random
from math import sqrt, floor
import emoji

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

print(random.randint(1, 10))  # número inteiro aleatório entre 1 e 10
print(random.random())  # número aleatório entre 0 e 1

print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))
