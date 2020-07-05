"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
a.	"Telefonou para a vítima?"
b.	"Esteve no local do crime?"
c.	"Mora perto da vítima?"
d.	"Devia para a vítima?"
e.	"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

pergunta1 = input('Telefonou para a vítima? ')
pergunta2 = input('Esteve no local do crime? ')
pergunta3 = input('Mora perto da vítima? ')
pergunta4 = input('Devia para vítima? ')
pergunta5 = input('Já trabalhou com a vítima? ')

respostas = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

def score(respostas):
    score = 0
    for i in respostas:
        if i.lower() == 'sim':
            score += 1
    if score == 5:
        print('Assassino')
    elif 3 <= score <= 4:
        print('Cúmplice')
    elif score == 2:
        print('Suspeita')
    else:
        print('Inocente')

score(respostas)