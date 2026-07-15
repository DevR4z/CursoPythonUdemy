from itertools import permutations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['João', 'Claudio', 'Luiz', 'Leticia']
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g']
]
print_iter(permutations(pessoas, 2))