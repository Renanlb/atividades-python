def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    print("Calculadora de Índice de Massa Corporal (IMC)")
    
    peso = float(input("Digite o seu peso em quilogramas: "))
    altura = float(input("Digite a sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Você está abaixo do peso.")
    elif imc < 24.9:
        print("Seu peso está dentro da faixa saudável.")
    elif imc < 29.9:
        print("Você está com sobrepeso.")
    elif imc < 34.9:
        print("Você está com obesidade grau 1.")
    elif imc < 39.9:
        print("Você está com obesidade grau 2.")
    else:
        print("Você está com obesidade grau 3 (obesidade mórbida).")

if __name__ == "__main__":
    main()