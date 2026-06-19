"""
Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p]
i - início (inclusivo)
f - fim (exclusivo)
p - passo (pula p caracteres)
"""

variavel = 'Olá Mundo'
print(variavel[0])  # O
print(variavel[1])  # l
print(variavel[4:])  # Mundo
print(variavel[:5])  # Olá M
print(variavel[4:7])  # Mun
print(variavel[0:9:2])  # OáMn