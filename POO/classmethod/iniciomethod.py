class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def meu_nome(cls, nome, idade):
        if nome == 'Rafael':
            print('Bom dia chará!')
        else: print(f'Bom dia {nome}! {idade}')

p1 = Pessoa.meu_nome('Rafael', 14)
print()
p2 = Pessoa.meu_nome('Julio', 27)
