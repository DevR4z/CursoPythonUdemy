class CallMe:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self, nome):
        print('Chamando', nome)
        return self.phone

call1 = CallMe('(31) 99476-2358')
contact = call1('Alan Minda')
print(contact)