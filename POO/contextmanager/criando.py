class FirstOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('Abrindo Arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf-8')
        return self._arquivo

    def __exit__(self, class_exception, exc, tb):
        print('Fechando Arquivo')
        self._arquivo.close()

        return True # Esconde o erro (usado para esconder tratar erro)

path_ = '.\\POO\\contextmanager\\criando.txt'
with FirstOpen(path_, 'w') as arquivo:
    arquivo.write('Linha pre\n')
    arquivo.write('Linha erro\n', 123)
    arquivo.write('Linha pos\n')
    print('With', arquivo)