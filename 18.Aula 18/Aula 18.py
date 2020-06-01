##### Aula 18 - Estruturas de Repetição 4: Repetições Encaixadas #####
'''
Peça para o usuário entrar com o início e o fim da tabuada
e imprima a tabuada correspondente dentro dos intervalos considerados
Exemplo:
Começo = 1
Fim = 3

Para o 1:
1X1 = 1
1X2 = 2
1X3 = 3

Para o 2:
2X1 = 2
2X2 = 4
2X3 = 6

Para o 3:
3X1 = 3
3X2 = 6
3X3 = 9
'''

# initial_value = int(input('Insert the initial value: '))
# end_value = int(input('Insert the final value: '))
#
# for i in range(initial_value, end_value+1):
#     for j in range(initial_value, end_value+1):
#         print('%dX%d=%d' %(i, j, i*j))
#
'''
Dados n e n sequencias de numeros inteiros não-nulos,
cada qual seguida por um 0,
calcular a soma dos números pares de cada sequencia
'''

n = int(input('Type the number of sequences: '))
print("")
for i in range(n):
    print('Sequence %i:' % (i+1))
    num = int(input('Type a number of the sequence: '))
    soma = 0
    while num != 0:
        if num % 2 == 0:
            soma += num
        num = int(input('Type a number of the sequence: '))
    print('The sum of sequence %i is %i'%(i+1, soma))
    print("")