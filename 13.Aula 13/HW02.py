"""
Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
"""

# Digitar o número n
n = int(input('Digite o valor de n: '))

# Imprimir os n primeiros números ímpares
count = 1
num = 1
impar_lista = [1]
while count < n:
    num += 2
    count += 1
    impar_lista.append(num)

print(impar_lista)