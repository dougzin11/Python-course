class Pessoa(object):
    pass

Lucas = Pessoa()
Lucas.nome = "Lucas"
Lucas.emprego = "Advogado"
Lucas.idade = 20
Lucas.cor_de_cabelo = "Preto"
print(Lucas.__dict__)

# Isso é muito parecido com a criação do dicionário abaixo
dicionario = {'Nome': 'Lucas', 'Emprego': 'Advogado', 'Idade': 20, 'Cor de Cabelo': 'Preto'}
print(dicionario)

# Como podemos ver, Python armazena os dados como dicionários. Isso faz com que Python seja uma linguagem menos eficiente!