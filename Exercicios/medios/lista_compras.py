import os

lista = []
conclusao = False

while conclusao == False:
    opcao = input('Selecione uma opção\n'
                  '[i]nserir [a]pagar [l]istar [f]echar: ')
    
    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)

    elif opcao == 'a':
        apagar = int(input('Escolha um indice para apagar: '))
        for i, nomes in enumerate(lista):
            if apagar == i:
                    lista.pop(i)
            else:
                    print('Não foi possivel apagar este índice')
    
    elif opcao == 'l':
        if lista == []:
            print('Nada para listar')
        else:
            os.system('cls')
            for indice, nome in enumerate(lista):
                print(indice, nome)
    
    elif opcao == 'f':
        conclusao = True
    