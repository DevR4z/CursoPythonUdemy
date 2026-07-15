import copy

from dados.produtos import produtos
#Aumente os preços dos produtos em 10% com deep copy
print('Aumento de 10%')
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1,2)}
    for p in copy.deepcopy(produtos)
    ]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()

#Ordene os produtos por nome decrescente
print('Ordenado por Nome decrescente')
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'], 
    reverse=True
)
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()

#Ordene por preço crescente
print('Ordenado por Preço crescente')
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
    )
print(*produtos, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')