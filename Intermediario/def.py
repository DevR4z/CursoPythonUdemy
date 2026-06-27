def saudacao(nome):
    print(f'Olá, {nome}!')

nome = input('Qual seu nome? ')
saudacao(nome)

def soma (x,y,z):
    print(f'{x=} {y=} {z=}', '|' 'x + y + z = ', x+y+z)

soma(1,2,3)
soma (1, y=2, z=5)