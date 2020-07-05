'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5! = 5.4.3.2.1 = 120. A saída deve ser conforme exemplo abaixo:

Fatorial de: 5
5! = 5 . 4 . 3 . 2 . 1 = 120
'''

def factorial(num):
    if num != 1:
        return num*factorial(num-1)
    else:
        return num

n = int(input('Fatorial de: '))
print(f'{n}! = ', end='')
for i in range(n, 0, -1):
    if i == 1:
        print(f'{i} = ', end=' ')
    else:
        print(f'{i} .', end=' ')
print(factorial(n))
