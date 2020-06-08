'''
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for
informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
- Mostre a quantidade de valores que foram lidos;
- Exiba todos os valores na ordem em que foram informados
- Exiba todos os valores na ordem inversa à que foram informados
- Calcule e mostre a soma dos valores;
- Calcule e mostre a média dos valores;
- Calcule e mostre a quantidade de valores acima da média calculada;
- Calcule e mostre a quantidade de valores abaixo de sete;
- Encerre o programa com uma mensagem;
'''

notas = []

nota = int(input('Insira o valor da nota: '))
soma = 0
while nota != -1:
    notas.append(nota)
    soma += nota
    nota = int(input('Insira o valor da nota: '))


print(f'Quantidade de notas lidas: {len(notas)}')
print(f'Lista de notas na ordem inserida: {notas}')
notas.reverse()
print(f'Lista de notas na ordem inversa: {notas}')
print(f'Soma das notas inseridas: {soma}')
print(f'Média das notas inseridas: {soma/len(notas)}')
print(f'Número de notas acima da média: {len([c for c in notas if c >= soma/len(notas)])}')
print(f'Número de notas abaixo de 7: {len([c for c in notas if c < 7])}')

print('Programa encerrado!')