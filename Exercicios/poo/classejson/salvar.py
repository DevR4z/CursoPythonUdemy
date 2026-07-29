import json
CAMINHO_ARQUIVO = '.\\Exercicios\\poo\\classejson\\classe.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('João', 27)
p2 = Pessoa('Julio', 37)
p3 = Pessoa('Tiago', 42)

dados = [p1.__dict__, p2.__dict__, p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    print('Dump raiz')
else: print('Dump externo')
    