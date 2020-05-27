'''
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes
na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro
notas de 1.
'''

# Ask for the value to withdraw
withdraw = int(input('Type the desired value to withdraw: '))

# Only allow withdraw if it is above 10 and lower than 600
if 10 <= withdraw <= 600:
    # Calculate the number of 100 bills
    bills_100 = withdraw // 100
    withdraw -= bills_100*100

    # Calculate the number of 50 bills
    bills_50 = withdraw // 50
    withdraw -= bills_50*50

    # Calculate the number of 10 bills
    bills_10 = withdraw // 10
    withdraw -= bills_10*10

    # Calculate the number of 5 bills
    bills_5 = withdraw // 5
    withdraw -= bills_5*5

    # The rest is in bills of 1
    if bills_100 != 0:
        print('Bills of R$ 100:', bills_100)
    if bills_50 != 0:
        print('Bills of R$ 50:', bills_50)
    if bills_10 != 0:
        print('Bills of R$ 10:', bills_10)
    if bills_5 != 0:
        print('Bills of R$ 5:', bills_5)
    if withdraw != 0:
        print('Bills of R$ 1:', withdraw)
else:
    print('Invalid value to withdraw!')