caminho_arquivo = 'C:\\Users\\rf001\\OneDrive\\Documentos\\CursoPythonUdemy\\Criacao de arquivo\\'
caminho_arquivo += 'aula116.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0,0)
    print(arquivo.read())