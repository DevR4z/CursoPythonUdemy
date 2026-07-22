def executa(funcao, *args):
    return funcao(*args)

print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5, 6,7))