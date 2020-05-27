'''
Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

Informe ao usuário a quantidade de latas de tinta a serem compradas
e o preço total.
'''
import math

# Specify the area to be painted
area = int(input('Please type the area (meters²) to be painted: '))

# Calculate the amount of liters needed (1 liter paints 3 meters squared)
liters = area/3

# Calculate the amount of gallons needed (1 gallon = 18 liters of paint)
gallons = math.ceil(liters/18)

# Calculate the amount needed to spend (1 gallon = R$ 80,00)
price = gallons*80

# Output the results
print('You need to buy', gallons, 'gallons of paint')
print('This will cost you R$', price)