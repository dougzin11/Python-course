'''
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula
    entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
    101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''

def verificar_int(input_number):
    try:
        input_number = float(input_number)
    except ValueError:
        print('Por favor insira um número inteiro!')
        return True
    else:
        x = not float(input_number).is_integer()
        if x:
            print('Por favor insira um número inteiro!')
        return x


def verificar_value(input_number):
    if float(input_number) > 1000:
        print('Por favor insira um número inteiro menor que 1000!')
        return True
    else:
        return False


def verificar_condicoes():
    i = True
    j = True
    while i or j:
        input_number = input('Insira um número inteiro: ')
        i = verificar_int(input_number)
        if not i:
            j = verificar_value(input_number)
    return int(input_number)


def print_numeros(input_number):
    # Calcular centenas
    centenas = input_number // 100
    input_number -= centenas * 100

    # Calcular dezenas
    dezenas = input_number // 10
    input_number -= dezenas * 10

    # Calcular unidades
    unidades = input_number

    # Definir condições
    centenas_exist = centenas != 0
    dezenas_exist = dezenas != 0
    unidades_exist = unidades != 0
    if centenas_exist and dezenas_exist and unidades_exist:
        print("%d centenas, %d dezenas e %d unidades" % (centenas, dezenas, unidades))
    elif centenas_exist and dezenas_exist and ~unidades_exist:
        print("%d centenas e %d dezenas" % (centenas, dezenas))
    elif centenas_exist and ~dezenas_exist and unidades_exist:
        print("%d centenas e %d unidades" % (centenas, unidades))
    elif ~centenas_exist and dezenas_exist and unidades_exist:
        print("%d dezenas e %d unidades" % (dezenas, unidades))
    elif ~centenas_exist and dezenas_exist and ~unidades_exist:
        print("%d dezenas" % dezenas)
    elif ~centenas_exist and ~dezenas_exist and unidades_exist:
        print("%d unidades" % unidades)
    elif centenas_exist and ~dezenas_exist and ~unidades_exist:
        print("%d centenas" % centenas)


input_number = verificar_condicoes()
print_numeros(input_number)