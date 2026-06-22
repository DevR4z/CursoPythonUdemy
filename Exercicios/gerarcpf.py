import re
import sys

cpf = input('Digite um CPF: ')
cpf = re.sub(r'[^0-9]', '', cpf)

validacao = cpf == cpf[0] * len(cpf)
if validacao:
    print('Dados sequenciais não são aceitos!')
    sys.exit()

cpf9 = cpf[:9]
cpf_tratado = []
i = 0
j = 0
contagem = [10,9,8,7,6,5,4,3,2]
soma = 0
#Tratamento dos números
while i < 9:
    cpf_tratado.append(int(cpf[i]))
    i += 1
# Soma
while j < len(cpf_tratado):
    soma += (cpf_tratado[j] * contagem[j])
    j += 1

multiplicacao = (soma * 10)
if multiplicacao % 11 > 9:
    digito1 = 0
else:
    digito1 = multiplicacao % 11

print(digito1)

#Segundo digito
i = 0
j = 0
soma = 0
contagem2 = [11,10,9,8,7,6,5,4,3,2]
cpf_tratado.append(digito1)
cpf_tratado2 = cpf_tratado

while j < len(cpf_tratado2):
    soma += (cpf_tratado2[j] * contagem2[j])
    j += 1

multiplicacao2 = (soma * 10)
if multiplicacao2 % 11 > 9:
    digito2 = 0
else:
    digito2 = multiplicacao2 % 11
print(digito2)

cpf_tratado.pop()
cpf_calculado = f'{cpf9}{digito1}{digito2}'
if cpf == cpf_calculado:
    print(f'{cpf} é válido')
else:
    print(f'CPF Invalido')
