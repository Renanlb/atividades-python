import random

numero_aleatorio = random.randint(1, 100)

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")

tentativas = 0

while True:
    tentativa = int(input("Tente adivinhar o número: "))
    tentativas += 1

    if tentativa < numero_aleatorio:
        print("O número é maior. Tente novamente.")
    elif tentativa > numero_aleatorio:
        print("O número é menor. Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_aleatorio} em {tentativas} tentativa(s)!")
        break
