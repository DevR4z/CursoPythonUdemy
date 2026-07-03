letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'r' in letras:
        print(f'Você acertou na tentativa {len(letras)}!😁')
        break

    print(letras)