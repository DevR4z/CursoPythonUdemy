# cria a def
def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

# faz a função com x receber o y na hora do print
def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

soma_com_cinco = criar_funcao(soma, 5) # função e o X
multiplica_por_dez = criar_funcao(multiplica, 10) # função e o X

print(soma_com_cinco(20)) # aqui vem o Y
print(multiplica_por_dez(3)) # aqui vem o Y