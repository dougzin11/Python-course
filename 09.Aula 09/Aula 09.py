##### Aula 09 - Estrutura de Decisões 1: if e else #####

idade = int(input("Type your age: "))

if idade >= 18:
    print("You can drink alcohol")
    if idade >= 21:
        print("You are VIP")
else:
    print("You cannot drink alcohol")

