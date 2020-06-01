##### Aula 19 - Operadores Lógicos #####
age = 40
if age >= 18 and age < 70:
    print('Welcome to the adulthood. Good luck')

'''
Dados três números naturais,
verificar se eles formam os lados de um triângulo retângulo

lado1**2 + lado2**2 == lado3**2
lado3**2 + lado1**2 == lado2**2
lado2**2 + lado3**2 == lado1**2
'''
# side1 = int(input('Type the value of the side: '))
# side2 = int(input('Type the value of the side: '))
# side3 = int(input('Type the value of the side: '))
#
# eval1 = side1**2 + side2**2 == side3**2
# eval2 = side3**2 + side1**2 == side2**2
# eval3 = side2**2 + side3**2 == side1**2
#
# if eval1 or eval2 or eval3:
#     print('The numbers form a triangle')
# else:
#     print('The numbers do not form a triangle')

'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um
número inteiro fornecido pelo usuário. O programa deverá mostrar também
o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes 
(divisões) executados
'''

N = int(input('Digite o valor de N: '))

div = 0
for i in range(1, N+1):
    primo = True
    j = 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo = False
        j += 1
    if primo:
        print(i)
print('Divisões realizadas: %d' %(div))