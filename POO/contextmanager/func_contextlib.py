from contextlib import contextmanager

@contextmanager
def my_archive(caminho_arquivo, modo):
    try:
        print('Abrindo Arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf-8')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()
        
path_ = '.\\POO\\contextmanager\\textcontextlib.txt'
with my_archive(path_, 'w') as arquivo:
    arquivo.write('Linha pre\n')
    arquivo.write('Linha mid\n', 123)
    arquivo.write('Linha pos\n')
    print('With', arquivo)