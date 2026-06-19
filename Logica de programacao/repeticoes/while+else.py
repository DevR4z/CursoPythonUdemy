nome = input('Digite somente seu primeiro nome: ')
i = 0

while i < len(nome):
    letra = nome[i]
    
    if letra == " ":
        break

    print(letra)
    i += 1
else:
    print('Nome totalmente soletrado!')
print('Fim.')