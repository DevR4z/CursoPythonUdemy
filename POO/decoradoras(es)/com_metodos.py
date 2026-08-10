def adc_repr(class_):
    def repr_(self):
        class_name = self.__class__.__name__
        class_repr = f'{class_name}: {self.nome}'
        return class_repr
    class_.__repr__ = repr_
    return class_

def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return f'({self.nome}) Esté é o nosso planeta'
        return resultado
    return interno

def meu_time(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Atletico Mineiro' in resultado:
            return f'Seu time é o Galão da Massa!'
        return resultado
    return interno

@adc_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
    @meu_time
    def qual_time(self):
        return f'Seu time é o {self.nome}'
@adc_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    @meu_planeta
    def qual_planeta(self):
        return f'O planeta é {self.nome}'

galo = Time('Atletico Mineiro')
palmeiras = Time('Palmeiras')
curitiba = Time('Curitiba')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(galo.qual_time())
print(palmeiras.qual_time())
print(curitiba.qual_time())
print()
print(terra.qual_planeta())
print(marte.qual_planeta())