"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""

# Os 3 candidatos são A, B e C
# Usuário digita o número de eleitores
n_eleitores = int(input('Digite o número de eleitores: '))

# Computar o voto de cada eleitor
count = 0
candidate_A = 0
candidate_B = 0
candidate_C = 0
while count < n_eleitores:
    voto = str(input('Digite o candidato: '))
    if voto == 'A':
        candidate_A += 1
    elif voto == 'B':
        candidate_B += 1
    elif voto == 'C':
        candidate_C += 1
    count += 1

print('Candidato A:', candidate_A)
print('Candidato B:', candidate_B)
print('Candidato C:', candidate_C)