# def print_iter(iterador):
#     print(*list(iterador), sep='\n)
    #   print()

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# aprovados = [
#     a for a in alunos
#     if a['nota'] == 'A'
# ]

aprovados = filter(
    lambda a: a['nota'] == 'A',
    alunos
)

print(*list(aprovados), sep='\n')