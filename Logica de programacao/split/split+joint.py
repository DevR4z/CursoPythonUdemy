frase = '  Olha só que    , coisa interessante    '
lista_frase_antiga = frase.split(',') #split() separa aonde voce pedir (',') <- na virgula

lista_frase = []
for i, frase in enumerate(lista_frase_antiga):
    lista_frase.append(lista_frase_antiga[i].strip()) #.strip tira os espaços

frases_juntas = ', '.join(lista_frase) # join junta uma string
print(frases_juntas)