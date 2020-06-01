"""
Dizemos que um inteiro positivo n é perfeito se for igual à soma de
seus divisores positivos diferentes de n.

Exemplo: 6 é perfeito, pois 1+2+3 = 6.
       Dado um inteiro positivo n, verificar se n é perfeito.
"""

# Usuário digitar o número n
n = int(input('Digite o número n: '))

# Encontrar os divisores de n
lista_divisores = []
for num in range(1, n+1):
    if n % num == 0 and num != n:
        lista_divisores.append(num)

# Verificar se a soma é igual a n
if sum(lista_divisores) == n:
    print(n, 'é um número perfeito')
else:
    print(n, 'não é um número perfeito')