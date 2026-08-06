from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg):
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool: pass

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.msg)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.msg)
        return False

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else: print('Notificação NÃO enviada')

notificar(NotificacaoEmail('Bom dia amigo'))

notificar(NotificacaoSMS('Testando SMS - Não enviar'))