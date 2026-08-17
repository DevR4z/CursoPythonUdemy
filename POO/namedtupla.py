from collections import namedtuple
from typing import NamedTuple


Carta = namedtuple('Carta', ['valor', 'naipe'])
sete_ouro = Carta('7', '♦️')
print(sete_ouro)
print(sete_ouro.naipe)
print(sete_ouro.valor)
print()


class Carta2(NamedTuple):
    valor: str = 'VALOR'
    naipe: str = 'NAIPE'


as_espadas = Carta2('A')
print(as_espadas._asdict())
