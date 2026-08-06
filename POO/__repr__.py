class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'

    def __add__(self, other):
        soma_x = self.x + other.x
        soma_y = self.y + other.y
        return Ponto(soma_x, soma_y)
    def __gt__(self, other):
        res_self = self.x + self.y
        res_other = other.x + other.y
        return res_self > res_other

if __name__ == '__main__':
    p1 = Ponto(4, 2)
    p2 = Ponto(6, 4)
    p3 = p1 + p2
    print(p3)
    print()
    print('P1 é maior que P2:', p1 > p2)
    print('P2 é maior que P1:', p2 > p1)