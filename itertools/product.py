from itertools import product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Claudio', 'Luiz', 'Leticia']
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
]
print_iter(product(*camisetas))