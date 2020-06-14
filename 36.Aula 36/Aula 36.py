##### Aula 36 - Funções 3: Variáveis globais e locais #####
'''
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma conta ou fechar o programa. Se
ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que o usuário selecione um número com 6 dígitos
e, então, se o número não existir no registro do banco, ele irá pedir um valor
de depósito. Depois o banco perguntará se deseja ver o saldo do banco, se
sim ele deverá imprimir o balanço geral do banco, senão ele entrará em loop
'''
contas = []
depositos = []
saldo = 0

def criaConta():
    global contas, depositos, saldo
    num_conta = int(input('Digite um número de conta: '))

    while num_conta in contas:
        print('Conta já existente. Digite novamente')
        num_conta = int(input('Digite um número de conta: '))

    contas.append(num_conta)

    deposito = float(input('Digite o valor do seu primeiro depósito: '))
    while deposito <= 0:
        print('Valor de depósito inválido')
        deposito = float(input('Digite o valor do seu primeiro depósito: '))

    depositos.append(deposito)
    saldo += deposito

def VerSaldo():
    global saldo
    opcao = bool(int(input('Deseja ver o saldo do banco (1-Sim, 0-Não): ')))
    if opcao:
        print(f'O saldo do banco é {saldo}')

def main():
    opcao = bool(int(input('Deseja criar conta(1) ou fechar programa(0): ')))
    while opcao:
        criaConta()
        VerSaldo()
        opcao = bool(int(input('Deseja criar conta(1) ou fechar programa(0): ')))

main()