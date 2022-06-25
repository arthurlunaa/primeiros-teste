"""
lista
lista em python funcional como vetores/matrizes (arrays) em outras linguagem,
com a diferença de ser (dinamico) e tambem podemos colocar ( qualquer tipo de dados

linguagem c/java:arrays
    - possuem tamanho e tipos de dados fixo:
    ou seja, nesta linguagem se voce criar um arrays do tipo int e tamanho 5 esse arrays sera sempre do tipo inteiro
    e podera ter sempre no maximo 5 valores.
    EM PYTHON
    dinamico: Não possuem tamanho fixo: ou seja podemos criar a lista e simplesmente ir adicionando elementos;
    qualquer tipo de dado: a lista não possem tipo de dado fixo ou seja podemos coloca tipo de dado

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista.
num = 7
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

#podemos facilmente ordena uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o numero de ocorrencia de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))


# adicionar elementos em lista

para adicionar elementos em listas, ultilizamos a função append

obs com apeend nos conseguimos adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # coloca a lista como elemento unico(sublista)
print(lista1)

if [8, 3 , 1 ] in lista1:
    print('Encontrei a lista')
else:
    print('não encontrei a lista')

lista1.extend([123, 44, 67]) # Coloca cada elemento da lista como valor adicional á lista.
print(lista1)
as lista em python são representanda por colchetes:[]
#podemos inserir um novo elemento na lista informando a posição do indice
lista1.insert(2, 'Novo valor')
print(lista1)

#podemos facilmente junta duas lista

lista6 =lista1 + lista2
print(lista6)
#podemos inverte uma lista facil usando reverse
#lista1.reverse()
#lista2.reverse()


print(lista1[::-1])
print(lista2[::-1])

#copiar uma lista

lista6 = lista2.copy()
print(lista6)

#podemos conta quantos elementos existem na lista.
print(len(lista5))

#podemos remover facil o ultimo elemento de uma lista
#obs pop nao somente remove o ultimo elemento como tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

#podemos remover um elemento pelo indices

lista5.pop(2)
print(lista5)
"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

#podemos remover todos elemento(mzera a lista