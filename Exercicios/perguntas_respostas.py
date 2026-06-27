# Sistema de perguntas e respostas
i = 0
escolha_int = None
acertou = False
qtd_acertos = 0

perguntas = [
    {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
},
{
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
},
{
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',
},
]

for questao in perguntas:
    print('Pergunta:', questao['Pergunta'])

    opcoes = questao['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    
    escolha = input('Escolha uma alternativa: ')

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < len(opcoes):
            if opcoes[escolha_int] == questao['Resposta']:
                acertou = True
    if acertou:
        qtd_acertos += 1
        print('Você acertou!!👌')
    else: print('Você errou.😬')
    
print('Você acertou', qtd_acertos, 'de', len(perguntas), 'Perguntas.')