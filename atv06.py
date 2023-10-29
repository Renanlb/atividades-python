import json
import os

arquivo_tarefas = "tarefas.json"

def verificar_arquivo_tarefas():
    if not os.path.exists(arquivo_tarefas):
        with open(arquivo_tarefas, "w") as arquivo:
            json.dump([], arquivo)

def carregar_tarefas():
    with open(arquivo_tarefas, "r") as arquivo:
        return json.load(arquivo)

def salvar_tarefas(tarefas):
    with open(arquivo_tarefas, "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def adicionar_tarefa(tarefas, descricao):
    nova_tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i}. [{status}] {tarefa['descricao']}")

def marcar_tarefa_concluida(tarefas, indice):
    if 0 < indice <= len(tarefas):
        tarefa = tarefas[indice - 1]
        tarefa["concluida"] = True
        salvar_tarefas(tarefas)
        print(f"A tarefa '{tarefa['descricao']}' foi marcada como concluída.")
    else:
        print("Índice de tarefa inválido.")

def remover_tarefa(tarefas, indice):
    if 0 < indice <= len(tarefas):
        tarefa = tarefas.pop(indice - 1)
        salvar_tarefas(tarefas)
        print(f"A tarefa '{tarefa['descricao']}' foi removida.")
    else:
        print("Índice de tarefa inválido.")

def main():
    verificar_arquivo_tarefas()
    tarefas = carregar_tarefas()

    while True:
        print("\nOpções:")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da nova tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(tarefas, indice)
        elif escolha == '4':
            listar_tarefas(tarefas)
            indice = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, indice)
        elif escolha == '5':
            print("Obrigado por usar o aplicativo de gerenciamento de tarefas. Tenha um bom dia!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
