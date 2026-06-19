condicao = True

while condicao:
    jogada = input('Qual o seu ataque? ')
    print(f'Você usou {jogada}')
    print('-' * 20)
    print('Digite "sair" para encerrar o jogo.')
    print('Ou jogue novamente!')
    print('-' * 20)

    if jogada == 'sair':
        print('Saindo do jogo...')
        break