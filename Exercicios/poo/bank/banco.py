import accounts
import pessoas


class Banco:
    def __init__(
            self,
            agencias: list[int] | None = None,
            clientes: list[pessoas.Pessoa] | None = None,
            contas: list[accounts.Conta] | None = None
            ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checar_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checar_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False

    def _checar_conta(self, conta):
        if conta in self.contas:
            return True
        return False

    def _checar_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: accounts.Conta):
        return self._checar_agencia(conta) and \
                self._checar_cliente(cliente) and \
                self._checar_conta(conta) and \
                self._checar_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = pessoas.Cliente('Rafael', 31)
    contacorrente1 = accounts.ContaCorrente(475, 322, 0, 0)
    c1.conta = contacorrente1

    c2 = pessoas.Cliente('Julia', 26)
    contapoupanca1 = accounts.ContaPoupanca(478, 665, 100)
    c2.conta = contapoupanca1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([contacorrente1, contapoupanca1])
    banco.agencias.extend([475, 249, 338, 111, 478])

    print(banco.autenticar(c1, contacorrente1))
    print(banco)
