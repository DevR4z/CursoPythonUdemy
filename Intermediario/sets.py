# Conjuntos em Python - Sets
s1 = set()
s1.add('Luiz')
s1.add(1)
s1.update(('Olá mundo', 1, 2, 3, 4, 3, 3))
s1.discard('Luiz')
# print(s1)

# Operadores:
#   |   Union
#   &   intersection (present in both)
#   -   difference (only on the left)
#   ^   symmetric difference (in just one set)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s2 - s1
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)