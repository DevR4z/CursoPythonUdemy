"""
Listas em Python
Tipo list - Mutável
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create, Read, Update, Delete = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
while len(lista) < 11:
    adicionar = input(f'Complete a lista {lista}. Adicionar: ')
    lista.append(adicionar)

print(f'Lista completa! {lista}')
print(f'Opss, foi um número a mais, vou remover o ultimo')
lista.pop()
print(f'Agora sim. {lista}')

lista.insert(0, 5)
print(f'Adicionei um {5} no inicio da lista.')
print(lista)