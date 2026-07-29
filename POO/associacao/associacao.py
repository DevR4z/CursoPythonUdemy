class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

        @property
        def ferramenta(self):
            return self._ferramenta
        @ferramenta.setter
        def ferramenta(self, ferramenta):
            self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, ferramenta_utilizando):
        self.ferramenta_utilizando = ferramenta_utilizando

    def escrever(self):
        return f'{self.ferramenta_utilizando} está escrevendo'

escritor = Escritor('Julio')
lapis = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Maquina')
escritor.ferramenta = maquina_de_escrever

print(lapis.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())