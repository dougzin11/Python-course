"""
Dados n e uma seqüência de n números inteiros,
determinar a soma dos números pares.
"""
# Usuário digita o número n
n = int(input('Digite o número n: '))

count = 0
lista_pares = []
while count < n:
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        lista_pares.append(num)
    count += 1

print(sum(lista_pares))