import emoji
import random
print(emoji.emojize('Seja muito Bem-Vindo ao meu mundo, ou melhor NOSSO mundo! :earth_americas:', use_aliases=True))
print('Você pode dar um nome ao mundo...')
mundo = input('Qual vai ser? ')
print(emoji.emojize('Ótimo nome! Seu :earth_americas: vai se chamar {}.'.format(mundo), use_aliases=True))
print(emoji.emojize('Antes de começar a construí-lo, quero saber mais sobre você... :blush:', use_aliases=True))
nome = input('Qual é o seu nome? ')
ano = int(input('Em que ano você nasceu? '))
idade = 2020 - ano
print('Muito bem {}!, então você tem aproximadamente {} anos.'.format(nome, idade))
acerto = input('Acertei? ')
print('Interessante...')
print('Você pode não acreditar, mas eu tenho somente 1 dia de idade...')
h = str(input('Qual é o seu passatempo favorito? '))
print(emoji.emojize('Uou, eu também gosto de {} :stuck_out_tongue_closed_eyes:'.format(h), use_aliases=True))
print('Vamos sair qualquer hora!')
print('Vou mostrar algumas coisas que eu posso fazer...')
print('Pera, agora que eu lembrei que eu não me apresentei kk\nPode me chamar de Golden!')
frase = str(input('Digite uma frase qualquer: ')).strip()
print('Boa! Sua frase possui {} caracteres contando os espaços.'.format(len(frase)))
print('Posso contar quantas letras A possui: {}'.format(frase.upper().count('A')))
print('Posso também colocar as primeiras letras em maiúsculo: {}'.format(frase.title()))
frase = frase.split()
print('E também seperar as palavras por hífen: {}'.format('-'.join(frase)))
print('Por fim, escolha 3 números: ')
n1 = input('Primeiro número: ')
n2 = input('Segundo: ')
n3 = input('Terceiro: ')
lista = [n1, n2, n3]
s = random.choice(lista)
print('Desses números o sorteado é: {}'.format(s))
print('Para me despedir eu coloco esse número na sua frase: {}'.format(' {} '.format(s).join(frase)))
e = input('Escolha outra coisa para por entre a sua frase: ')
print('Boa escolha haha\n{}'.format('{}'.format(e).join(frase)))
print('Por hoje é só! Espero te encontrar na próxima!')