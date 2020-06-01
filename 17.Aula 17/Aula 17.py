##### Aula 17 - Estruturas de Repetição 3: Ciclo for e range #####
'''
Calcule n! usando o for loop
'''

# Ask the user to input the number n
n = int(input('Type the value of n: '))
factorial = 1
for i in range(n, 1, -1):
    factorial *= i
print('%d! = %d' % (n, factorial))

'''
Um numero triangular é calculado pela fórmula
triangular = n * (n+1) / 2
Sendo n o índice desse número triangular
Escreva um programa que imprima os números triangulares com índices
múltiplos de 5 entre 5 e 50

primeiro triangular = 1
segundo triangular = 3
'''
for n in range(5, 51, 5):
    print('%d index: triangular value = %d' %(n, n*(n+1)/2))