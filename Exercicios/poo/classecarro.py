class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, modelo):
        self._motor = modelo

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fab):
        self._fabricante = fab


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

# Fabricantes


volkswagen = Fabricante('Volkswagen')
chevrolet = Fabricante('Chevrolet')
fiat = Fabricante('Fiat')
honda = Fabricante('Honda')
toyota = Fabricante('Toyota')

# Motores
motor1_0 = Motor('1.0')
motor1_6 = Motor('1.6')
motor2_0 = Motor('2.0')

fusca = Carro('Fusca')
fusca.fabricante = volkswagen
fusca.motor = motor1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

astra = Carro('Astra')
astra.fabricante = chevrolet
astra.motor = motor1_6
print(astra.nome, astra.fabricante.nome, astra.motor.nome)

etios = Carro('Etios')
etios.fabricante = toyota
etios.motor = motor2_0
print(etios.nome, etios.fabricante.nome, etios.motor.nome)

civic = Carro('Civic')
civic.fabricante = honda
civic.motor = motor1_6
print(civic.nome, civic.fabricante.nome, civic.motor.nome)
