'''
Escreva um programa que crie uma lista de elementos, até se entrar -1,
e depois imprima todos os números da lista que são maiores que 10
'''

vetor =[]
num = int(input('Digite um numero: '))

while num != -1:
    vetor.append(num)
    num = int(input('Digite um numero: '))

for element in vetor:
    if element > 10:
        print(element)