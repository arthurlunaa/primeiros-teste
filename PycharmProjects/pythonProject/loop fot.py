"""
Loop for-> Estrutura de repetição.]
for-> Uma dessas estruturas

# Exemplo de for 1 interagindo sting
nome = 'Arthur Henrique'
lista = [1, 3, 5, 7, 9]
numero : range = range(1, 10)



for letra in nome:
    print(letra)

#exemplo de for 2 (interando sobre lista)

for numero in lista:
    print(numero)

# exemplo de for 3 interando sobre range

for numero in range(1, 10):
    print(numero)
    for indice,letra in enumerate(nome):
    print(nome[indice])

for indice,letra in enumerate(nome):
    print(letra)
for _,letra in enumerate(nome):
    print(letra)
for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor)
    nome = 'Arthur Henrique'
lista = [1, 3, 5, 7, 9]
numero: range = range(1, 10)
qtd =int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):c
   num = int(input(f'informe 0 {n}/{qtd} valor:'))
   soma = soma + num
print(f'A soma é {soma}')

nome = 'Arthur Henrique'

for letra in nome:
    print(letra, end='')
"""
# original U+1F60D
# modificado U0001f60d

for _ in range(3):
    for num in range (1, 11):
        print(f'\U0001F60D' * num)
