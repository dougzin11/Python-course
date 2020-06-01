##### Aula 14 - Estruturas de Repetição 2: Nested while loops #####
'''
Dado um numero n de empresas, e um numero m de meses,
e o ganho e gastos positivos e inteiros de cada empresa para cada mes,
imprimir se a empresa nesses meses ficou com défict, lucro ou indiferente
e imprimir o valor correspondente a essa balança

Exemplo de execução:
Digite o numero de empresas: 3
Digite o numero de meses: 2

Empresa 1:
Mes 1:
Digite o ganho da empresa no mes: 500
Digite o gasto da empresa no mes: 500

Mes 2:
Digite o ganho da empresa no mes: 600
Digite o gasto da empresa no mes: 600

A empresa 1 ficou indiferente (balança = R$ 0)

Empresa 2:
Mes 1:
Digite o ganho da empresa no mes: 500
Digite o gasto da empresa no mes: 600

Mes 2:
Digite o ganho da empresa no mes: 800
Digite o gasto da empresa no mes: 1000

A empresa 2 ficou déficit de R$ - 300

Empresa 3:
Mes 1:
Digite o ganho da empresa no mes: 800
Digite o gasto da empresa no mes: 500

Mes 2:
Digite o ganho da empresa no mes: 1100
Digite o gasto da empresa no mes: 1000

A empresa 3 ficou com lucro de R$ 400
'''

companies = int(input('Type the number of companies: '))
months = int(input('Type the number of months to take into account: '))

comp = 1
while comp <= companies:
    print('Company', comp)
    month = 1
    total_revenue = 0
    total_costs = 0
    while month <= months:
        revenue = int(input('Revenue for company %d - M%d: ' % (comp, month)))
        costs = int(input('Costs for company %d - M%d: ' % (comp, month)))
        total_revenue += revenue
        total_costs += costs
        balance = total_revenue - total_costs
        month += 1
    if balance < 0:
        print('Company %d is in deficit of R$ %d' % (comp, balance))
    elif balance > 0:
        print('Company %d is in profit of R$ %d' % (comp, balance))
    else:
        print('Company %d has a balance equal to 0' % (comp))
        month += 1
    comp += 1
    print('\n')