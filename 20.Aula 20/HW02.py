"""
Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer
as consistências, informando ao usuário nas seguintes situações:

    a.	Se o usuário informar o valor de A igual a zero, a equação não é do
    segundo grau e o programa não deve pedir os demais valores,
    sendo encerrado;

    b.	Se o delta calculado for negativo, a equação não possui raizes reais.
    Informe ao usuário e encerre o programa;

    c.	Se o delta calculado for igual a zero a equação possui apenas uma raiz
    real; informe-a ao usuário;

    d.	Se o delta for positivo, a equação possui duas raiz reais; informe-as
    ao usuário;
"""

a = float(input('Digite o valor de a: '))
if a == 0:
    print('A equação não é do segundo grau. Programa encerrado')
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    delta = b**2 - 4*a*c
    if delta < 0:
        print('O programa não possui raízes reais. Programa encerrado')
    elif delta == 0:
        raiz = -b / (2*a)
        print('A equação possui uma única raíz igual a %f' % (raiz))
    else:
        raiz_positiva = (-b + (delta)**(1/2)) / (2*a)
        raiz_negativa = (-b - (delta)**(1/2)) / (2*a)
        print('A equação possui as seguintes raízes: %f e %f'
              % (raiz_positiva, raiz_negativa)
            )