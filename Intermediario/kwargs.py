pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}

def argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# argumentos_nomeados(1, 2, 3, nome='Rafael', idade=22)
argumentos_nomeados(**pessoa_completa)