##### Aula 31 - Listas: Métodos pop, index, insert, sort, clear e copy #####
'''
Crie uma lista, peça para o usuário escolher um indice da lista, imprima
o elemento da lista neste índice e o remova da lista,
depois imprima a lista
'''

a = [3, 2, 3, 4, 5]

print(a)

indice = int(
    input(
        f'Digite o indice (0 até {len(a)} do elemento a ser removido: '
    )
)

print('Elemento:', a.pop(indice))
print(a)

'''
Escreva um programa que recebe um número x e devolve o primeiro índice
de uma lista que contem o elemento x. Caso x não esteja na lista, imprima
uma mensagem adequada
'''

a = [1, 2, 4, 4, 5]

x = int(input('Digite o valor de x: '))

print(a.index(x))

'''
Escreva um programa em que dado a posição i e um número qualquer x,
deve-se inserir essa elemento numa lista na posição determinada

Ex:
lista = [1, 2, 3, 4]
Digite a posição: 2
Digite o elemento: 8000
lista = [1, 2, 8000, 3, 4]
'''

a = [1, 2, 3, 4]

print('lista =', a)

pos = int(input('Digite a posição: '))
ele = int(input('Digite o elemento: '))

a.insert(pos, ele)
print('lista =', a)

'''
Organize os elementos de uma lista em ordem crescente
'''

a = [5,3,1,2,4]
print(a)
a.sort()
print(a)