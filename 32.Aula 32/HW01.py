'''
Reescreva o simulador da megasena de forma que agora em vez de trabalhar
com o mesmo jogo sempre, o programa seleciona aleatoriamente o jogo
teórico do jogador. Faça apenas um teste.
'''
import random

n = int(input('Digite o número de simulações: '))
megasena = list(range(1,61))
soma = 0

for i in range(n):
    # Criar um jogo aleatório
    jogo_aleatorio = megasena.copy()
    meu_jogo = []
    for j in range(6):
        escolhido = random.choice(jogo_aleatorio)
        meu_jogo.append(escolhido)
        jogo_aleatorio.remove(escolhido)

    meu_jogo.sort()

    # Criar variáveis de sorteio
    jogo_sorteado = []
    cont = 0

    while jogo_sorteado != meu_jogo:
        lista_sorteio = megasena.copy()
        jogo_sorteado = []

        for j in range(6):
            sorteado = random.choice(lista_sorteio)
            jogo_sorteado.append(sorteado)
            lista_sorteio.remove(sorteado)

        jogo_sorteado.sort()
        cont += 1

    soma += cont

    print(f'Resultado do teste {i + 1}: {cont} tentativas')

soma /= n

print('Média dos resultados', soma)