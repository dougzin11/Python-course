'''
Faça um programa para uma loja de tintas

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a titna é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os
respectivos preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 4 litros;
- misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
'''

import math

# Ask for the area to be painted
area = float(input('Type the area(meters²) to be painted): '))

# Increase by 10%
area *= 1.1

# Arredondar area
area = math.ceil(area)

# Calculate the number of liters needed
liters = math.ceil(area/6)

print('Liters needed:', liters)

gallons_18 = math.ceil(liters/18)
print('1) Buy only gallons of 18 liters:')
print(gallons_18, 'liters')
print('R$', gallons_18*80)
print('\n')

gallons_4 = math.ceil(liters/4)
print('2) Buy only gallons of 4 liters:')
print(gallons_4, 'liters')
print('R$', gallons_4*25)
print('\n')

# Gallons of 18 are cheaper than gallons of 4
# We will fill as much as we can with gallons of 18 and the
# remaining with gallons of 4
gallons_mix_18 = liters//18
reamining_liters = liters - gallons_mix_18*18
gallons_mix_4 = math.ceil(reamining_liters/4)
print('3) Buy mix:')
print('gallons of 18 liters:', gallons_mix_18, 'liters')
print('gallons of 4 liters:', gallons_mix_4, 'liters')
print('R$', gallons_mix_18*80 + gallons_mix_4*25)
print('\n')
