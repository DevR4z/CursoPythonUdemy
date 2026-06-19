"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r, !s, !a
"""

variavel = 'ABC'
print(f'{variavel: >10}')  # Alinhado a direita
print(f'{variavel: <10}')  # Alinhado a esquerda
print(f'{variavel: ^10}')  # Alinhado ao centro
print(f'{1000.78146291283:+,.1f}')  # Sinal, separador de milhar e 1 casa decimal