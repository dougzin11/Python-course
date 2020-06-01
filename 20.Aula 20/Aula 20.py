##### Aula 20 - Reais, As variáveis do tipo float #####
'''
Dado um inteiro positivo n, calcular e imprimir o valor da seguinte soma:
S = 1/n + 2/(n-1) + 3/(n-2) + ... + n/1
'''

n = int(input('Digite o valor de n: '))
soma = 0

for i in range(1, n+1):
    soma += i/(n - i + 1)

print('Soma é igual a %.2f' % (soma))

'''
Faça um programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média por igual a 10
'''

media = float(input('Digite a primeira nota do aluno: '))
media += float(input('Digite a segunda nota do aluno: '))
media += float(input('Digite a terceira nota do aluno: '))

media /= 3
if 7 <= media != 10:
    print("Aprovado. Sua média foi de %.2f" % (media))
elif media < 7:
    print("Reprovado. Sua média foi de %.2f" % (media))
else:
    print("Aprovado com Distinção. Sua média foi de 10.0")