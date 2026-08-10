"""Modulo de exemplo

Funções e exemplos de documentação de funções.
"""
v1 = 1

def soma(x: int | float, y: int | float) -> int | float:
    return x + y

def multiplica(
        x: int | float,
        y: int | float,
        z: int | float | None = None
) -> int | float:
    """Multiplica x, y e/ou z

    Multiplica x e y. Se z for enviado, multiplica x, y, z.
    """
    if z is None:
        return x * y
    return x * y * z

v2 = 2
v3 = 3
v4 = 4