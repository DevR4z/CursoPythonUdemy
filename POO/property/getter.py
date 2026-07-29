class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
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