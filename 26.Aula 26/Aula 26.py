##### Aula 26 - Listas dentro de Listas, Adicionar novos elementos #####
lista = [1, 2, 3, 4, [1, 2, 3, 4]]
# Obtendo o 5 elemento (lista) e o terceiro elemento dessa lista
print(lista[4][2])

# Lista formada por 2 listas
lista = [[[1,2], [3,4]], [5,6]]

# Primeira lista formada por outras 2 listas
print(lista[0][0])
print(lista[0][1])
print(lista[1])
print(lista[0])

'''
Faça um programa que leia um vetor de 5 números inteiros e mostre-os
'''
vetor = []
for i in range(1, 6):
    num = int(input(f'Digite o número {i} de 5: '))
    vetor.append(num)

print(vetor)