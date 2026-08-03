class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property #property retorna / setter "faz a fução"
    def cor(self):
        print('@Property')
        return self.cor_tinta
    @property
    def tampa(self):
        print('Cor da tampa')
        return 'Preta'

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.tampa)
print()
print(caneta.cor)