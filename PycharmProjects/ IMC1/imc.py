altura = float(input('Qual é sua altura em cm:'))
peso = float(input('Qual é seu peso em kg:'))

IMC = peso/(altura/100)**2

print (IMC)

if IMC < 18:
    print(f'Seu IMC é de {IMC}, e é classificado com0 Magreza')

elif IMC >= 18.5 and IMC < 24.9:
    print(f'Seu IMC é de {IMC}, e é classificado como Normal')

elif IMC >= 25 and IMC 29.9:
    print(f'Seu IMC é de {IMC}, e é classificado como Sobre-peso')

elif IMC>= 30 and IMC 39.9:
    print(f'Seu IMC é de {IMC}, e é classificado como obeso')

else:
    print("pode para de comer esta foda projetinho")

#18,5 a 24,9	Adequado
#25,0 a 29,9	Pré-Obeso
#30,0 a 34,9	Obesidade Grau I
#35,0 a 39,9	Obesidade Grau II