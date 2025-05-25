import json
import os
import time

compras = {}

def adicionar_item(compras, item, quantidade):
    """
    Adiciona um item com a quantidade especificada à lista de compras.
    """
    compras[item] = quantidade

def remover_item(compras, item):
    """
    Remove um item da lista de compras, se ele existir.
    """
    if item in compras:
        del compras[item]

def visualizar_compras(compras):
    """
    Exibe a lista de compras no terminal.
    """
    for item, quantidade in compras.items():
        print(f'{item}: {quantidade}')
    print()
    input('Pressione Enter para continuar...')

def salvar_compras(compras, nome_arquivo):
    """
    Salva a lista de compras em um arquivo JSON.
    """
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    """
    Carrega a lista de compras a partir de um arquivo JSON.
    """
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras, nome_arquivo=None):
    """
    Menu de gerenciamento da lista de compras.
    Permite adicionar, remover, visualizar, salvar ou sair.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1 - Adicionar item")
        print("2 - Remover item")
        print("3 - Visualizar lista")
        print("4 - Salvar e sair")
        print("5 - Sair sem salvar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input('Digite o nome do item: ')
            quantidade = float(input('Digite a quantidade: '))
            adicionar_item(compras, item, quantidade)

        elif escolha == "2":
            item = input('Digite o nome do item: ')
            remover_item(compras, item)

        elif escolha == "3":
            visualizar_compras(compras)

        elif escolha == "4":
            if nome_arquivo is None:
                nome_arquivo = input('Digite o nome do arquivo para salvar: ')
            if not nome_arquivo.endswith(".json"):
                nome_arquivo += ".json"
            salvar_compras(compras, nome_arquivo)
            break

        elif escolha == "5":
            break

        else:
            print('Opção inválida')
            time.sleep(1)

def main():
    """
    Menu principal do programa.
    Permite criar uma nova lista ou carregar uma existente.
    """
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print('1 - Criar uma nova lista de compras')
        print('2 - Carregar uma lista existente')
        print('3 - Sair')
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            compras = {}
            gerenciar_compras(compras)

        elif escolha == "2":
            print("Listas Disponíveis:")
            arquivos = [arquivo for arquivo in os.listdir() if arquivo.endswith(".json")]
            
            if not arquivos:
                print("Nenhuma lista encontrada.")
                time.sleep(1)
                continue

            for i, arquivo in enumerate(arquivos, 1):
                print(f'{i} - {arquivo}')
                
            try:
                escolha = int(input("Escolha uma lista para carregar (0 para cancelar): "))
            except ValueError:
                print("Entrada inválida.")
                time.sleep(1)
                continue

            if escolha == 0:
                continue

            if escolha < 0 or escolha > len(arquivos):
                print("Opção inválida.")
                time.sleep(1)
                continue

            nome_arquivo = arquivos[escolha - 1]
            compras = carregar_compras(nome_arquivo)
            gerenciar_compras(compras, nome_arquivo)

        elif escolha == "3":
            break

        else:
            print('Opção inválida.')
            time.sleep(1)

if __name__ == "__main__":
    main()
