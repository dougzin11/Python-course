'''
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa
um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso
'''

h = float(input('Digite a altura em metros:'))
p = float(input('Digite o peso em kg: '))
s = str(input('Digite o seu sexo (M ou F): '))

if s == M:
    ideal = 72.7*h - 58
else:
    ideal = 62.1&h - 44.7

if p > ideal:
    print("Acima do peso")
elif p == ideal:
    print("Dentro do peso")
else:
    print("Abaixo do peso")