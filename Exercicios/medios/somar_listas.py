l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
soma = [x + y for x, y in zip(l1, l2)]

print(soma)

# lista_soma = []
# for i in range(len(l2)):
#     lista_soma.append(l1[i] + l2[i])
# print(lista_soma)