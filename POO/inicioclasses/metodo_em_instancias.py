class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        if self.nome == 'Fusca':
            print(f'{self.nome} acelera a 60km/h')

        else:   print(f'{self.nome} acelera a 78km/h')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()