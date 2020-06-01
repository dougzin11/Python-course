"""
Dado um número inteiro positivo n,
calcular a soma dos n primeiros números inteiros positivos.
"""

# Digitar o número n
n = int(input('Digite o valor de n: '))

count = 1
total = 0
while count <= n:
    num = int(input('Digite o número da sequência: '))
    total += num
    count += 1
print('Soma dos números é', total)