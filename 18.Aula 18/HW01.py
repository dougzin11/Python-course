"""
Dados dois naturais m e n determinar, entre todos os pares de números naturais
(x,y) tais que x < m e y < n, um par para o qual o valor da expressão
x*y - x**2 + y seja máximo e calcular também esse máximo.
"""

# Pedir valores de m e n para o usuário
m = int(input('Digite o valor de m: '))
n = int(input('Digite o valor de n: '))

# Obter conjunto de pares possíveis e armazenar em uma lista
lista_pares = []
for i in range(m):
    for j in range(n):
        lista_pares.append([i, j])

# Calcular a expressão para cada par, armazenando apenas o valor máximo
maximum = -np.inf
for par in lista_pares:
    valor = par[0] * par[1] - par[0] ** 2 + par[1]
    if valor > maximum:
        maximum = valor
        x = par[0]
        y = par[1]
print('Valor máximo é:', maximum)
print('Esse valor é obtido pelo par [%d, %d]' % (x, y))