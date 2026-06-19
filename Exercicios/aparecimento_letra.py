frase = "Rafael Ferreira Abranches"\
        "Bianca Gabriela"

i = 0
aparecimento = 0
letra = ''
while i < len(frase):
    letra_atual = frase[i]
    aparecimento_atual = frase.count(letra_atual)

    if aparecimento < aparecimento_atual:
        aparecimento = aparecimento_atual
        letra = letra_atual

    i += 1
print(f'A letra que apareceu mais vezes foi a letra "{letra}" com {aparecimento}x')