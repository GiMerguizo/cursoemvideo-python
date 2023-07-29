from time import sleep

print('\033[31mDesafio 024\033[m')
c = str(input('Qual é o nome da sua cidade? ')).strip()
c = c.lower().split()
print('\033[35mAnalisando sua cidade...\033[m')
sleep(2)
s = 'santo' in c[0]
if not s:
    v = '\033[31m'
else:
    v = '\033[32m'
print('Sua cidade começa com \033[36mSanto\033[m. Isso é {}{}\033[m.'.format(v, 'santo' in c[0]))
# print(c[0] == 'santo')
print('Obs.: \033[32mTrue = verdadeiro\033[m / \033[31mFalse = falso\033[m')
