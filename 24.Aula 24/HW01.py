'''
Escreva um programa para simular o jogo das portas. Faça um programa
que tenha a saída como a seguinte:

Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro
ou não!
Escolha uma porta: 3
Você escolheu a porta 3, mas eu lhe informa que na porta 2 há um bode.
Deseja trocar de porta (1 - Sim / 0 - Não) - 1
Ganhou um carro!
'''
# With this problem we will tackle the famous Monty Hall problem
# Instead of the program showed in the description, we will show
# empirically why the user should always change the initial door chosen

import random

print('Welcome to the Monty Hall problem demonstration program!')

runs = int(input('Please type the number of times you wish to play the game: '))

not_switched = 0
switched = 0
for run in range(runs):
    # The candidate chooses randomly one door
    chosen_door = random.randrange(1, 4)

    # The car is in one of the doors
    car_door = random.randrange(1, 4)

    # The door that opens cannot be the one with the car or
    # the one that the candidate chose
    opened_door = random.randrange(1, 4)
    while opened_door == car_door or opened_door == chosen_door:
        opened_door = random.randrange(1, 4)

    # Lets simulate when the candidate change the door
    switch_door = [
        c for c in [1, 2, 3] if c != opened_door and c != chosen_door
    ][0]

    # Lets count now how many times the candidate would win
    # switching and not switching while playing the game
    if switch_door == car_door:
        switched += 1
    else:
        not_switched += 1

print(f'If the candidate switches, he would win {switched/runs*100}% of the time')
print(f'If the candidate does not switch, he would win {not_switched/runs*100}% of the time')
