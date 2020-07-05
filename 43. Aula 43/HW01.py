"""
Escreva o jogo do chute.
Nele você deve sortear um número inteiro entre 1 e 100 e pedir
para o usuário advinhar o número que você escolheu

Para cada chute do usuário você deve imprimir uma dica, se
ele chutou baixo de mais ou alto demais

Uma vez que o usuário acerte o chute o programa imprime uma
mensagem e também o número de chutes que o usuário deu

OBS: Use o statement break

Exemplo:

>>>
Tente advinhar o número que eu estou pensando
Seu Chute: 50
Você deve chutar mais alto!
Seu Chute: 75
Você deve chutar mais alto!
Seu Chute: 87
Você deve chutar mais alto!
Seu Chute: 93
Você deve chutar mais alto!
Seu Chute: 97
Você deve chutar mais baixo!
Seu Chute: 95
Parabens você acertou!!
Você chutou 6 vezes
>>>

"""
import random

def sortNum():
    return random.randint(1, 100)


def main():
    sorted_num = sortNum()
    win = False
    cont = 0
    while win == False:
        guess = int(input('Digit your guess: '))
        cont += 1
        if sorted_num > guess:
            print('Guess a higher number!')
        elif sorted_num < guess:
            print('Guess a lower number!')
        else:
            break

    print('Congratulations, you won!')
    print(f'Number of guesses: {cont}')

main()