"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)
    if numero_int % 2 ==0:
        print(f'O numero {numero_int} é par')
    else:
        print(f'O numero {numero_int} é ímpar')
except:
    print('Você não digitou um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input('Digite a HORA atual: ')

try:
    hora_int = int(hora_str)
    if 0 <= hora_int <= 11:
        print('Bom dia!')
    elif 12 <= hora_int <= 17:
        print('Boa tarde!')
    elif 18 <= hora_int <= 23:
        print('Boa noite!')
except:
    print('Digite somente a Hora atual em números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
nome_tamanho = len(nome)
if nome_tamanho > 1:
    if nome_tamanho <= 4:
            print('Seu nome é curto')
    elif 5 <= nome_tamanho <= 6:
            print('Seu nome tem um tamanho normal')
    elif nome_tamanho > 6:
            print('Seu nome é grande')
else:
     print('Digite um nome válido')
