import csv
import os

def criar_arquivo_csv():
    if not os.path.exists('agenda.csv'):
        with open('agenda.csv', mode='w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(['Nome', 'Telefone'])

def adicionar_contato(nome, telefone):
    with open('agenda.csv', mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, telefone])

def listar_contatos():
    with open('agenda.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            print(f'Nome: {row[0]}, Telefone: {row[1]}')

def buscar_contato(nome):
    with open('agenda.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            if row[0] == nome:
                print(f'Nome: {row[0]}, Telefone: {row[1]}')
                return
        print('Contato não encontrado.')

def remover_contato(nome):
    linhas = []
    with open('agenda.csv', mode='r') as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            if row[0] != nome:
                linhas.append(row)
    
    with open('agenda.csv', mode='w', newline='') as arquivo:
        writer = csv.writer(arquivo)
        for row in linhas:
            writer.writerow(row)

criar_arquivo_csv()

while True:
    print("\nOpções:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Remover contato")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif escolha == '2':
        listar_contatos()
    elif escolha == '3':
        nome = input("Digite o nome do contato a ser buscado: ")
        buscar_contato(nome)
    elif escolha == '4':
        nome = input("Digite o nome do contato a ser removido: ")
        remover_contato(nome)
    elif escolha == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")
