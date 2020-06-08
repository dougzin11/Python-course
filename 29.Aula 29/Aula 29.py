##### Aula 29 - For loops e Listas #####
'''
Faça um programa que peça as quatro notas de 10 alunos, calcule e amerazene
num vetor a média de cada aluno, imprima o número de alunos com média maior
ou igual a 7.0
'''

alunos = 10
vetor = []
passou = 0
for aluno in range(1,alunos+1):
    nota = float(input(f'Digite a nota 1 do aluno {aluno}: '))
    nota += float(input(f'Digite a nota 2 do aluno {aluno}: '))
    nota += float(input(f'Digite a nota 3 do aluno {aluno}: '))
    nota += float(input(f'Digite a nota 4 do aluno {aluno}: '))
    media = nota/4
    vetor.append(media)
    if media >= 7:
        passou += 1
    print(nota)
    nota = 0

print(f'Numero de alunos com média maior ou igual a 7.0: {passou}')