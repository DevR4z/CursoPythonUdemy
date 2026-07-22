import os
import json

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
        print('Criando arquivo...')
        return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'Exercicios\\medios\\lista_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        print()
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas')
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        print()
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    print()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        print()
        return

    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


while True:
    salvar(tarefas, CAMINHO_ARQUIVO)
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
 
    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
