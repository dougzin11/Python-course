"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.

o	Faça um programa que recebe o salário de um colaborador e o
        reajuste segundo o seguinte critério, baseado no salário atual:

o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.

"""

salario_inicial = float(input('Digite o salário do colaborador: '))

if salario_inicial < 280:
    percentual = 20
    salario_ajus = salario_inicial*(1 + percentual/100)
elif 280 <= salario_inicial < 700:
    percentual = 15
    salario_ajus = salario_inicial*(1 + percentual/100)
elif 700 <= salario_inicial < 1500:
    percentual = 10
    salario_ajus = salario_inicial*(1 + percentual/100)
else:
    percentual = 5
    salario_ajus = salario_inicial*(1 + percentual/100)

print('Salário antes do reajuste: R$ %5.2f' % (salario_inicial))
print('Percentual de aumento aplicado: %i%%' % (percentual))
print('Valor do aumento: R$ %5.2f' % (salario_ajus - salario_inicial))
print('Salário pós aumento: R$ %5.2f' % (salario_ajus))