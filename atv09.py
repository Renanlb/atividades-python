import os

def exibir_filmes():
    print("Filmes em exibição:")
    for i, filme in enumerate(filmes, 1):
        print(f"{i}. {filme['titulo']} ({filme['horario']}) - {filme['disponibilidade']} assentos disponíveis")

def fazer_reserva(filme_indice, quantidade):
    filme = filmes[filme_indice - 1]
    if filme['disponibilidade'] >= quantidade:
        filme['disponibilidade'] -= quantidade
        print(f"Reserva confirmada: {quantidade} ingresso(s) para '{filme['titulo']}' ({filme['horario']}).")
        salvar_reserva(filme['titulo'], quantidade)
    else:
        print("Desculpe, não há assentos disponíveis suficientes para essa reserva.")

def salvar_reserva(filme, quantidade):
    with open("reservas.txt", "a") as arquivo:
        arquivo.write(f"{filme}: {quantidade} ingresso(s)\n")

filmes = [
    {"titulo": "Filme 1", "horario": "10:00", "disponibilidade": 100},
    {"titulo": "Filme 2", "horario": "13:00", "disponibilidade": 75},
    {"titulo": "Filme 3", "horario": "16:00", "disponibilidade": 50},
]

def main():
    print("Bem-vindo ao Sistema de Reservas de Cinema!")

    while True:
        exibir_filmes()
        escolha = input("Escolha um filme (número) ou digite 'sair' para sair: ")

        if escolha.lower() == "sair":
            print("Obrigado por usar o Sistema de Reservas de Cinema. Tenha um bom dia!")
            break

        try:
            filme_indice = int(escolha)
            if 1 <= filme_indice <= len(filmes):
                quantidade = int(input("Quantos ingressos deseja reservar? "))
                fazer_reserva(filme_indice, quantidade)
            else:
                print("Filme inválido. Tente novamente.")
        except ValueError:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
