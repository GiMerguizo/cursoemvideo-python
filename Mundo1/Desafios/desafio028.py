import random
from time import sleep  # faz o computador "dormir" por alguns segundos
print('\033[31mDesafio 028\033[m')
print('\033[93m-=-\033[m' * 20)
print('\033[34mVamos jogar! Eu vou pensar num número entre 0 e 5 e você tenta adivinhar!\033[m')
print('\033[93m-=-\033[m' * 20)
num = int(input('Qual número você acha que é? '))
print('\033[32mPROCESSANDO...\033[m')
sleep(3)
lista = [0, 1, 2, 3, 4, 5]
s = random.choice(lista)  # random.randint(0, 5)
if num == s:
    print('\033[35mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('Que pena, não foi dessa vez. O número que eu escolhi foi \033[91m{}\033[m.'.format(s, num))
