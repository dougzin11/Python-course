##### Aula 44 - Strings 1: Introdução #####
'''
Faça um programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.

Observadno os termos no plural a colocação do "e", da vírgula entre
outros. Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades

Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20,
10, 21, 11, 1, 7 e 16
'''

lista = [
    326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21,
    11, 1, 7, 16
]

for number in lista:
    intact_number = number
    centenas = number//100
    number -= centenas*100

    dezenas = number//10
    number -= dezenas*10

    saida = str(intact_number) + ' = '

    if centenas > 0:
        saida += str(centenas) + ' centena'
        if centenas > 1:
            saida += 's'

        if dezenas > 0 and number != 0:
            saida += ', '
        elif dezenas > 0:
            saida += ' e '
        else:
            if number > 0:
                saida += ' e '
    if dezenas > 0:
        saida += str(dezenas) + ' dezena'
        if dezenas > 1:
            saida += 's'
        if number > 0:
            saida += ' e '

    if number > 0:
        saida += str(number) + ' unidade'
        if number > 1:
            saida += 's'

    print(saida)