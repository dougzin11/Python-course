##### Aula 69 - Exceções 3: Clausulas do bloco try #####

try:
    lista = []
    lista.append(int('1'))
except (IndexError, ValueError) as excessao:
    print(excessao)
    print('ERRO!!')
else:
    print('tudo deu certo')
finally:
    print('Finalmente')