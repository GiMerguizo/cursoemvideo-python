nome = str(input('Qual é o seu nome? '))
if nome == 'Giovana':
    print('Que nome bonito!')
elif nome == 'Enzo' or nome == 'Valentina':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Maria Pedro Paulo João Mateus Tiago Eva':
    print('Belo nome bíblico!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
