"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar
M-matutino ou V-Vespertino ou N- Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
"Valor Inválido!", conforme o caso.
"""

print('M - Matutino \t V - Vespertino \t N - Noturno')
turno = input('Digite o turno em que estuda: ')

if turno.lower() == 'm':
    print('Bom dia!')
elif turno.lower() == 'v':
    print('Boa tarde!')
elif turno.lower() == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido!')