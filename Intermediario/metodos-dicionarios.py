# Metodos úteis do dicionario
pessoa = {
    'nome': 'Rafael Ferreira',
    'sobrenome': 'Abranches',
}
# len - conta keys
print('Len')
print(len(pessoa))
print('-'*15)

# keys - retorna as keys
print('Keys')
print(list(pessoa.keys()))
for chave in pessoa:
    print(chave)
print('-'*15)    

# values - retorna os valores
print('Values')
print(list(pessoa.values()))
for valor in pessoa.values():
    print(valor)
print('-'*15)

# items - return keys and values
print('Items')
print(list(pessoa.items()))
for key, value in pessoa.items():
    print(key, value)
print('-'*15)

# copy - faz uma copia do dicionaria de referencia 
# (somente dados mutaveis são alterados no copy)
# para copia profunda, import copy and use copy.deepcopy()

# get - obtém a chave
print('Get')
print(pessoa.get('nome', None))
print('-'*15)

# pop - apaga o item com a chave especificada (del)
# print(pessoa['nome']) key error 
print('Pop')
nome = pessoa.pop('nome')
print(nome)
print(pessoa)
print('-'*15)

# popitem - apaga a ultima chave

# update - Atualiza o dicionario - Adiciona ou modifica
print('Update')
pessoa.update({
    'nome': 'Rafael (Updated)',
    'idade': 20,
})
print(pessoa)