##### Aula 40 - Funções 4: Nested Functions e Nonlocal #####
'''
Escreva uma nested function que forneça um número (x da função menor) elevado
a outro (N da função maior)
'''

def exp(N):
    def eleva(X):
        print(X**N)
    return eleva

f = exp(3)
f(2)

def f1():
    X = 1
    def f2():
        nonlocal X
        print(X)
        X += 1
    return f2

g = f1()
g()
g()
g()
g()