'''
Dados dois números inteiros positivos i e j diferentes de 0,
imprimir todos os divisores comuns de i e j.

Exemplo: i = 2 e j = 3 a saída deverá ser : 1
i = 9, j = 21 a saída deverá ser: 1, 3
'''

i = int(input('Digite o primeiro número: '))
j = int(input('Digite o segundo número: '))

number = 1
while number <= min(i,j):
    eval1 = i % number == 0
    eval2 = j % number == 0
    if eval1 and eval2:
        print(number)
    number += 1
