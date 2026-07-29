class Camera:
    def __init__(self, nome, on=False):
        self.nome = nome
        self.on = on

    def filmar(self):
        if self.on:
            print('Já esta filmando, desligue se quiser gravar novamente.')
            return
        print(f'{self.nome} Ligando...')
        print(f'{self.nome} Começou a filmar!')
        self.on = True

    def desligar(self):
        if self.on:
            self.on = False
            print(f'{self.nome} Desligada.')
        else: print(f'{self.nome} Não estava ligada.')

c1 = Camera('Canon')
c1.filmar()
c1.filmar()
c1.desligar()
c1.desligar()