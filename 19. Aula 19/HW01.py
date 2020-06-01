'''
Dado n e dois números inteiros positivos i e j diferentes de 0,
imprimir em ordem crescente os n primeiros naturais que são múltiplos de i
ou de j e ou de ambos.

Ex: Para n = 6, i = 2 e j = 3 a saída deverá ser : 0, 2, 3, 4, 6, 8
'''

n = int(input('Digite o valor de n: '))
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))

output = []
number = 0
quantity = 0
while quantity < n:
    eval1 = number % i == 0
    eval2 = number % j == 0
    if eval1 or eval2:
        print(number)
        quantity += 1
    number += 1