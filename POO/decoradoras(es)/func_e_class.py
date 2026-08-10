def adc_repr(class_):
    def repr_(self):
        class_name = self.__class__.__name__
        class_repr = f'{class_name}: {self.nome}'
        return class_repr
    class_.__repr__ = repr_
    return class_

@adc_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
@adc_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

galo = Time('Atletico Mineiro')
palmeiras = Time('Palmeiras')
curitiba = Time('Curitiba')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(galo)
print(palmeiras)
print(curitiba)
print()
print(terra)
print(marte)