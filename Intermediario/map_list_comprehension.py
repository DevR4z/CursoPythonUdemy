# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} #isso cai no if
    if produto['preco'] > 20  else {**produto} # else só retorna sem modificar
    for produto in produtos
   #if produto['preco'] > 10
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')