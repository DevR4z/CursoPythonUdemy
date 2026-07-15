import index_package.modulo
from index_package import modulo
from index_package.modulo import * # __all__ filtrado em modulo.py

# from index_package.modulo import soma_do_modulo

print(soma_do_modulo(1, 2))
print(index_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
# print(nova_variavel) # não definido em __all__