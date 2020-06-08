##### Aula 30 - Listas: Métodos reverse e remove #####
'''
Peça uma lista de números inteiros para o usuário e imprima a
lista sem repetições
'''

n  = int(input('Digite o número de elementos da lista: '))

lista = []
aux = []
for i in range(n):
    elemento = int(input('Digite o elemento %i de %i: ' % (i+1, n)))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for i in aux:
    for j in range (lista.count(i)-1):
        lista.remove(i)

print(lista)