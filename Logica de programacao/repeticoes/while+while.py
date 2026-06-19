qtd_linhas = 5
qtd_colunas = 5
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    print(f'{linha=}')

    while coluna <= qtd_colunas:
        print(f'{coluna=}', end=' ')
        coluna += 1

    print()  # Imprime uma quebra de linha após cada linha da tabela
    print()  # Espaçamento entre as linhas da tabela
    linha += 1