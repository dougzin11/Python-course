##### Aula 47 - Strings 4: Padrão ASCII, Comparações e Operador in #####
'''
Faça duas funções: uma que coloque uma string em maiusculo e outra
que coloque uma string em minusculo
'''

def main():
    string = 'CHiCleTe'

    print(tudoMinusculo(string))
    print(tudoMaiusculo(string))

def tudoMinusculo(string):
    minusculo = ""

    for char in string:
        if 'A' <= char <= 'Z':
            char = chr(ord(char) + (ord('a') - ord('A')))
        minusculo += char

    return minusculo

def tudoMaiusculo(string):
    maiusculo = ''

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        maiusculo += char

    return maiusculo

main()