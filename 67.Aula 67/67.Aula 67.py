##### Aula 67 - Exceções 1: Introdução #####

x = input('Digite um número: ')
try:
    x = int(x)
except:
    print('Por favor insire um número inteiro')
    x = 0
finally:
    print(x)