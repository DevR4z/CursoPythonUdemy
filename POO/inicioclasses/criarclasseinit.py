class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Rafael', 'Ferreira')
p2 = Pessoa('Luiz', 'Otávio')

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
