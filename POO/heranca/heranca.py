class Pessoa:
    cpf = '000.000.000-00'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    cpf = '173.545.420.30'

c1 = Cliente('Luiz', 'Otavio')
c1.falar_nome_classe()
print(c1.cpf)

a1 = Aluno('João', 'Victor')
a1.falar_nome_classe()
print(a1.cpf)