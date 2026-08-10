class Somar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador

@Somar
def soma(x, y):
    return x + y

calc = soma(2,5)
print(calc)