# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    total = 1
    for num in args:
        total *= num
    return total

multiplicacao = mult(2,3,10)
print(multiplicacao)

def multiplicar(numero, vezes):
    return numero * vezes
print(multiplicar(2,4))

# Crie uma funções que fala se um número é par ou ímpar.

def resto(a):
    if a % 2 == 0:
        return f'{a} é par'
    return f'{a} é ímpar'

print(resto(multiplicacao))