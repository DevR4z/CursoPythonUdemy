import enum

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    CIMA = enum.auto()
    BAIXO = enum.auto()

print(Direcoes.ESQUERDA, Direcoes.ESQUERDA.name)
print(Direcoes(2), Direcoes(2).name)
print()

def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name}')

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.BAIXO)
mover(Direcoes.CIMA)
