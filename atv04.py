saldo = 1000.0

def consultar_saldo():
    print(f"Seu saldo atual é: R${saldo:.2f}")

def sacar_dinheiro(valor):
    global saldo
    if valor > 0 and saldo >= valor:
        saldo -= valor
        print(f"Você sacou: R${valor:.2f}")
        print(f"Seu saldo atual é: R${saldo:.2f}")
    else:
        print("Saldo insuficiente ou valor de saque inválido.")

def depositar_dinheiro(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print(f"Você depositou: R${valor:.2f}")
        print(f"Seu saldo atual é: R${saldo:.2f}")
    else:
        print("Valor de depósito inválido.")

def main():
    print("Bem-vindo ao Caixa Eletrônico")
    
    while True:
        print("\nOpções:")
        print("1. Consultar Saldo")
        print("2. Sacar Dinheiro")
        print("3. Depositar Dinheiro")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            consultar_saldo()
        elif escolha == '2':
            valor = float(input("Digite o valor que deseja sacar: R$"))
            sacar_dinheiro(valor)
        elif escolha == '3':
            valor = float(input("Digite o valor que deseja depositar: R$"))
            depositar_dinheiro(valor)
        elif escolha == '4':
            print("Obrigado por usar o Caixa Eletrônico. Tenha um bom dia!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
