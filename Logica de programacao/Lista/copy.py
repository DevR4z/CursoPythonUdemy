lista_a = ['Rafael','Julio','Maria']
lista_b = lista_a.copy()
condicao = False
i = 0

while condicao == False:
    try:
        chegadas = int(input('Quantas pessoas novas chegaram? '))
        if type(chegadas) == int:
            condicao = True
    except:
        print('Digite um numero!')
while i < chegadas:
    novo_membro = input('Chegou um novo membro chamado: ')
    lista_a.append(novo_membro)
    i += 1
print(f'No inicio era {lista_b}')
print(f'Agora somos {lista_a}')