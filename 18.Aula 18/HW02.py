"""
Sabe-se que um número da forma n**3 é igual a soma de n ímpares consecutivos.

Exemplo: 1**3= 1, 2**3= 3+5, 3**3= 7+9+11,  4**3= 13+15+17+19,...
Dado m, determine os ímpares consecutivos cuja soma é igual a n**3 para n
assumindo valores de 1 a m.
"""

# Pedir ao usuário valor de m
m = int(input('Digite o valor de m: '))

# Lista nula
subset_list = []

for n in range(1, m + 1):
    print('O número', n, 'elevado ao cubo tem como soma: ', end='')

    # Lista de valores impares
    impar_list = [c for c in range(1, n ** 3 + 1) if c % 2 != 0]

    if n == 1:
        print([1])
    else:
        for i in range(len(impar_list)):
            for j in range(i + 1, len(impar_list)):
                if sum(impar_list[i:j]) == n ** 3:
                    print(impar_list[i:j])