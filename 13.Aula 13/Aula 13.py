##### Aula 13 - Estruturas de Repetição 1: while #####
'''
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função potência
da linguagem
'''

number1 = int(input('Type the first number: '))
number2 = int(input('Type the second number: '))

count = 1
result = 1
while count <= number2:
    result *= number1
    count += 1
print(number1, '^', number2, '=', result)

'''
Dado um número inteiro não negativo n, determinar n!
5! = 5*4*3*2*1 = 120
4! = 3*2*1 = 6
'''

number = int(input('Type a non negative number: '))
initial_number = number

if number < 0:
    print('Invalid number')
else:
    result = 1
    while number > 1:
        result *= number
        number -= 1
print(initial_number, '! =', result)

'''
Dada uma sequencia de números inteiros não-nulos,
seguida por 0, imprimir seus quadrados
'''

user_input = int(input('Type a number: '))
while user_input != 0:
    print(user_input, "^2 =", user_input**2)
    user_input = int(input('Type a number: '))