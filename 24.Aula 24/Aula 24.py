##### Aula 24 - Números pseudo Aleatórios: Módulo random #####
'''
Escreva um programa para testar se a estatística proposta no filme
'Quebrando a banca' é verdadeora. Utilize o módulo random para tais testes.
'''
import random

testes = int(input('Digite o número de testes: '))

trocar = 0
n_trocar = 0

for i in range(testes):
    porta = random.randrange(1, 4)
    premio = random.randint(1, 3)

    if porta == premio:
        n_trocar += 1
    else:
        trocar += 1

print(f"É vantajoso trocar em {trocar/testes*100}% das vezes")
print(f'Não é vantajoso trocar em {n_trocar/testes*100}% das vezes')