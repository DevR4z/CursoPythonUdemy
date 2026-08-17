import abc


class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        pass

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'(Depósito: {valor})')
        return self.saldo

    def detalhes(self, msg='') -> None:
        print(f'O seu saldo é {self.saldo:.2f}, {msg}')
        print()

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(Saque: {valor})')
            return self.saldo
        print('Não tem saldo suficiente para esse saque')
        self.detalhes(f'(Saque Negado: {valor})')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_max = -self.limite

        if valor_pos_saque >= limite_max:
            self.saldo -= valor
            self.detalhes(f'(Saque: {valor})')
            return self.saldo
        print('Não tem saldo suficiente para esse saque')
        print(f'Seu limite é de {+self.limite:.2f}')
        self.detalhes(f'(Saque Negado: {valor})')
        return self.saldo

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
                f'{self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    contapoupanca1 = ContaPoupanca(432, 1, 0)
    contapoupanca1.sacar(1)
    contapoupanca1.depositar(1)
    contapoupanca1.sacar(1)
    contapoupanca1.sacar(1)
    print()
    contacorrente1 = ContaCorrente(432, 2, 0, 100)
    contacorrente1.sacar(1)
    contacorrente1.depositar(1)
    contacorrente1.sacar(50)
    contacorrente1.sacar(50)
    contacorrente1.sacar(1)
    print()
