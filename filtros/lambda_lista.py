lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda', 'idade': 19},
    {'nome': 'Maria', 'sobrenome': 'Oliveira', 'idade': 15},
    {'nome': 'Daniel', 'sobrenome': 'Silva', 'idade': 30},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira', 'idade': 26},
    {'nome': 'Aline', 'sobrenome': 'Souza', 'idade': 10},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['idade'])

exibir(l1)
exibir(l2)