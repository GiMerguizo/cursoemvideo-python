import emoji
from time import sleep
print('\033[31mDesafio 046\033[m')
print('-=' * 20)
print('\033[35mContagem Regressiva\033[m')
print('-=' * 20)
# e = emoji.emojize(':boom:', use_aliases=True)
f = emoji.emojize(':fireworks:', use_aliases=True)
# som = emoji.emojize('/play secret', use_aliases=True)
print('PREPARA-SE!!!')
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
# print(som)
print('FELIZ ANO NOVO {}{}{}!!!!!'.format(f, f, f))
