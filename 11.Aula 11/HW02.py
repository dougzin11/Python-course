'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''


def min_max_numbers(number1, number2, number3):
    # Listar numeros
    lista = [number1, number2, number3]
    maximo = max(lista)
    minimo = min(lista)
    print('Maior número é', maximo)
    print('Menor número é', minimo)



a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

min_max_numbers(a, b, c)