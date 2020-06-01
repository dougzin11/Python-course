##### Aula 21 - Interagindo inteiros com reais, arredondamento #####
'''
Faça um programa que peça 2 números inteiros e um número real
Calcule e mostre:
- o produto do dobro do primeiro com metade do segundo
- a soma do triplo do primeiro com o terceiro
- o terceiro elevado ao cubo
'''

int1 = int(input('Digite o primeiro número inteiro: '))
int2 = int(input('Digite o segundo número inteiro: '))
real = float(input('Digite um número real: '))

print((2*int1)*(int2/2))
print(3*int1 + real)
print(real**3)

'''
Faça um programa que peça um número e informe se o número é inteiro ou decimal.
Se o número for decimal, arredonde o número
'''
num = float(input('Digite um número: '))
if int(num) != num:
    decimal = num - int(num)
    arredondado = int(num)

    if decimal >= 0.5:
        arredondado += 1
    print(num, 'é decimal')
    print('Arredondando:', arredondado)
else:
    print(num, 'é inteiro')