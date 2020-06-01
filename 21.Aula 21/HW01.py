'''
Dado x real e n natural, calcular uma aproximação para cos x através dos
n primeiros termos da seguinte série:
cos x = 1/1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ... + ((-1)**k)*(x**2k)/(2k!)

Compare com os resultados de sua calculadora
'''

x = float(input('Digite um número real: '))
n = int(input('Digite um número natural: '))

approx = 1
elemen = 1
for i in range(1, n+1):
    elemen *= (-(x**2)/(2*i*(2*i-1)))
    approx += elemen

print('O cosseno de ', x, 'é', approx)