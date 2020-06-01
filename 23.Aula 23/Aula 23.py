##### Aula 23 - Utilizando Módulos: Módulo math #####
'''
Faça um programa que peça o raio de um círculo, calcule e mostre sua área
'''
from math import pi

raio = float(input('Digite o raio do círculo: '))
area = pi*(raio**2)

print('A área do círculo de raio %.2f é %.2f' % (raio, area))