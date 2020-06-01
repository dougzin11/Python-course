"""
Faça um programa que leia dez conjuntos de dois valores,
o primeiro representando o número do aluno e o segundo representando a sua
altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com
suas alturas.

"""

menor_numero = maior_numero = int(input('Digite o seu número: '))
menor_altura = maior_altura = float(input('Digite a sua altura: '))

for i in range(9):
    numero = int(input('Digite o seu número: '))
    altura = float(input('Digite a sua altura: '))

    if altura < menor_altura:
        menor_altura = altura
        menor_numero = numero

    if altura > maior_altura:
        maior_altura = altura
        maior_numero = numero

print("O Aluno de numero %i tem a maior altura(%.2f m)"%(maior_numero, maior_altura))
print("O Aluno de numero %i tem a menor altura(%.2f m)"%(menor_numero, menor_altura))
