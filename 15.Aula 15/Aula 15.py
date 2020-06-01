##### Aula 15 - Dois atalhos em Python #####
'''
Dizemos que um número natural é triangular se ele é produto de três
números naturais consecutivos.

Exemplo: 120 é triangular, pois 4.5.6 = 120
Dado um inteiro não-negativo n, verificar se n é triangular
'''

# Type the number to evaluate
n = int(input('Type the number to evaluate: '))

# Calculate the possible products
cont = 3
found = False
while (cont) * (cont - 1) * (cont - 2) <= n:
    if (cont) * (cont - 1) * (cont - 2) == n:
        print(
            '%i is a triangular number. It is equal to %i*%i*%i'
            % (n, cont, cont-1, cont-2)
        )
        found = True
        break
    cont += 1

if not found:
    print(n, 'is not a triangular number')

'''

'''