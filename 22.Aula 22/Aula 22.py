# ##### Aula 22 - A função print: formatação #####
# '''
# O Departamento Estadual de Meteorologia lhe contratou para desenvolver
# um programa que leia um conjunto indeterminado de temperaturas, e informe
# ao final a menor e a maior temperaturas informadas, bem como a média das
# temperaturas
# '''
#
# num = int(input('Digite o número de temperaturas registradas: '))
#
# soma = maior = menor = float(input("Digite a temperatura 1: "))
#
# for i in range(2, num+1):
#     temp = float(input("Digite a temperatura %d: " % (i)))
#
#     if temp > maior:
#         maior = temp
#
#     if temp < menor:
#         menor = temp
#
#     soma += temp
#
# print('A maior temperatura é %6.2f ºC' % (maior))
# print('A menor temperatura é %6.2f ºC' % (menor))
# print('A média das temperaturas é %6.2f ºC' % (soma/num))

'''
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma
As turmas não podem ter mais de 40 alunos.
'''

turmas = int(input('Digite a quantidade de turmas: '))

soma = 0
for i in range(1, turmas+1):
    qtde = int(input('Digite o número de alunos da turma %d: ' %i))
    while qtde > 40 or qtde < 0:
        print('Número de alunos inválido')
        qtde = int(input('Digite o número de alunos da turma %d: ' % i))
    soma += qtde

print('A média dos alunos é %.2f alunos por turma' % (soma/turmas))