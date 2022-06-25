""""
Recebendo dados do usuário
"""
# Entrega de dados
# print ("Qual é o seu nome?")
# #nome = input()
nome = input ('Qual é seu nome?')
# Processamento

# Saida de dados
#print(' Seja bem-vindo(a) %s' % nome)
#print('Seja bem-vindo(a) {0}'.format (nome))

print(f'Seja bem-vindo(a) {nome}')

# Entrega de dados

#print('Qual é sua idade ?')
#idade = input()
idade = int(input('Qual é a sua idade?'))

# Processamento

# saida
#print ('A %s tem %s anos'% (nome , idade))
#print('A {0} tem {1} anos'.format (nome, idade))
print (f'A {nome},tem {idade} anos')

print(f'A {nome} nasceu em {2022 -(idade)}')