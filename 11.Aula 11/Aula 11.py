##### Aula 11 - Estrutura de Decisões 2: if, elif e else #####

'''
Faça um programa que leia um número e exiba o dia correspondente da semana.
(1 - Domingo, 2 - Segunda, etc.), se digitar outro valor deve aparecer
valor inválido
'''
dia = int(input('Digita o dia da semana: '))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido")