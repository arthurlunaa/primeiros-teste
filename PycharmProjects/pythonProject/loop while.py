from ex0001 import idade

print("Qual é seu nome")
nome = ''
resposta = ''
while resposta != 'sim':
    nome = input()
    resposta = input()

idade

if idade < 18:
    print('Menor de idade')
