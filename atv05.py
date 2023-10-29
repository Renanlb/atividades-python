taxas_de_cambio = {
    "USD": 1.0,         # Dólar Americano 
    "EUR": 0.85,        # Euro 
    "GBP": 0.75,        # Libra Esterlina 
}

# Função para converter moedas
def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem in taxas_de_cambio and moeda_destino in taxas_de_cambio:
        taxa_origem = taxas_de_cambio[moeda_origem]
        taxa_destino = taxas_de_cambio[moeda_destino]
        valor_convertido = valor * (taxa_destino / taxa_origem)
        return valor_convertido
    else:
        return None

# Função principal do programa
def main():
    print("Bem-vindo ao Conversor de Moedas")
    
    while True:
        print("\nOpções:")
        print("1. Converter Moeda")
        print("2. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, GBP): ").upper()
            moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, GBP): ").upper()
            
            if moeda_origem == moeda_destino:
                print("As moedas de origem e destino são as mesmas.")
                continue
            
            valor = float(input("Digite o valor a ser convertido: "))
            
            resultado = converter_moeda(valor, moeda_origem, moeda_destino)
            
            if resultado is not None:
                print(f"{valor} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")
            else:
                print("Moeda não suportada.")
        elif escolha == '2':
            print("Obrigado por usar o Conversor de Moedas. Tenha um bom dia!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
