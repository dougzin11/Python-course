"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os dois vetores.
"""

vetor_par = []
vetor_impar = []

for i in range(1,21):
    num = float(input(f'Digite o número {i}: '))
    if num % 2 == 0:
        vetor_par.append(num)
    else:
        vetor_impar.append(num)

print('Vetor par:', vetor_par)
print('Vetor impar:', vetor_impar)