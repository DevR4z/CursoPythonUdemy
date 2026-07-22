def adc_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adc_clientes('Luiz')

adc_clientes('Rafael', cliente1)

cliente2 = adc_clientes('João')
adc_clientes('Mara', cliente2)

print(cliente1)
print(cliente2)