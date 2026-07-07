def zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por Zero')
    return True

def nao_e_numero(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. \n'
            f'"{tipo_n.__name__}" enviado'
            )
    return True
    
def divide(n, d):
    nao_e_numero(n)
    nao_e_numero(d)
    zero(d)
    return n / d

print(divide(8, '0'))