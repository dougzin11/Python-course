##### Aula 28 - Listas: Função len e Método Count #####
'''
Recebendo entradas inteiras do usuário que só devem ser interrompidas com a
entrada do número -1, e recebendo um elemento qualquer, calcualr o número
de vezes que esse elemento aparece na sequência digitada pelo usuário
'''

lista = []

num = int(input('Digite um número da sequência: '))

while num != -1:
    lista.append(num)
    num = int(input('Digite um número da sequência: '))

elemento = int(input('Digite o elemento a ser procurado: '))

print(f'O elemento {elemento} aparece {lista.count(elemento)} vezes na sequência')


'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes
e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor
foi conseguido.
'''
import random

resultados = []

n = int(input('Digite o número de lançamentos: '))
for i in range(n):
    resultados.append(random.randint(1,6))

for i in range(1,7):
    print(f'A face {i} foi obtida {resultados.count(i)/n*100}%')
