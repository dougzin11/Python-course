##### Aula 48 - Strings 5: Métodos de Strings 1, Cifra de César #####

TAM_MAX_CH = 26

def recebeModo():
    '''
    Função que pergunta se o usuário quer criptografar ou decriptografar
    e garante que uma entrada válida foi recebida
    '''

    entrada = input('Você deseja criptografar ou decriptografar?\n')
    while True:
        if entrada in 'criptografar c decriptografar d'.split():
            return entrada
        else:
            print('Entrada inválida. Entre "criptografar" ou "c" ou "decriptografar" ou "d"')
            entrada = input('Você deseja criptografar ou decriptografar?\n')

def recebeChave():
    '''
    Função que pede o valor da chave para o usuário e devolve a chave
    caso o valor desta esteja adequado
    '''

    global TAM_MAX_CH

    while True:
        chave = int(input(f'Entre o número da chave (1-{TAM_MAX_CH})\n'))
        if 1 <= chave <= TAM_MAX_CH:
            return chave

def geraMsgTraduzida(entrada, mensagem, chave):
    '''
    Traduz a mensagem do usuário de modo conveniente
    '''
    if entrada[0] == 'd':
        chave *= -1

    traduzido = ''

    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            traduzido += chr(num)
        else:
            traduzido += simbolo

    return traduzido


def main():
    """
    Função principal do programa
    """
    entrada = recebeModo()
    mensagem = input("Entre sua mensagem\n")
    chave = recebeChave()

    print("Seu texto traduzido é:")
    print(geraMsgTraduzida(entrada, mensagem, chave))

main()
