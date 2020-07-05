"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5
Segundo Salto: 6.1
Terceiro Salto: 6.2
Quarto Salto: 5.4
Quinto Salto: 5.3

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

def name():
    return input('Atleta: ')

def saltos():
    first = float(input('First jump: '))
    second = float(input('Second jump: '))
    third = float(input('Third jump: '))
    fourth = float(input('Forth jump: '))
    fifth = float(input('Fifth jump: '))
    return [first, second, third, fourth, fifth]

def calculate(l):
    count = 0
    soma = 0
    for el in l:
        soma += el
        count += 1
    return soma / count

def imprimir(nome, lista, media):
    print('\n')
    print('Resultado Final:')
    print('Atleta:', nome)
    print(f'Saltos: {lista[0]} - {lista[1]} - {lista[2]} - {lista[3]} - {lista[4]}')
    print(f'Média dos saltos: {media} m')

def main():
    nome = name()
    while nome:
        lista = saltos()
        media = calculate(lista)
        imprimir(nome, lista, media)
        nome = name()

main()