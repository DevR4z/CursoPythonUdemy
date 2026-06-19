'''"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra = 'Rafael'
sua_palavra = []
tentativas = 1
i = 0
j = 0
k = 0
chances = len(palavra)
chute = ''
while i < len(palavra):
    sua_palavra.append(' ')
    i += 1

while j < len(palavra):
    print(f'{tentativas}° Tentativa, você tem mais {len(palavra) - j} chances')
    tentativas += 1
    palpite = input('Digite apenas uma letra: ')
    
    while k < len(palavra):
        if palpite == palavra[0:100]:
            sua_palavra.replace(sua_palavra[k],palpite)
            k += 1
        else:
            k += 1

    j += 1

print(f'Você chegou nessa palavra: {sua_palavra}, tente adivinhar:')
'''

palavra = 'Rafael'
sua_palavra = ['_'] * len(palavra)
tentativas = 0

while tentativas < len(sua_palavra):
    print(' '.join(sua_palavra))
    print(f'Você possui {len(palavra) - tentativas} tentativas!')
    palpite = input('Digite uma letra: ').strip()

    if len(palpite) != 1:
        print('Digite apenas uma letra.')
        continue

    tentativas += 1

    for i in range(len(palavra)):
        if palpite.lower() == palavra[i].lower():
            sua_palavra[i] = palavra[i]

print(f'Você acertou a palavra: {"".join(sua_palavra)}')
print(f'Total de tentativas: {tentativas}')