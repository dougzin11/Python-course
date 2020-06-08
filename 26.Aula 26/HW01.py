'''
Faça um programa que leia 4 notas, mostre as notas e a média na tela
'''

notas = []
soma = 0
for i in range(1, 5):
    num = float(input(f'Digite a nota da prova {i}: '))
    notas.append(num)
    soma += num

for i in range(1, 5):
    print(f'Nota {i}: {notas[i-1]}')

print(f'A média é {soma/4}')