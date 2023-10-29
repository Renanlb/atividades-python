import random

palavras = ["python", "javascript", "java", "ruby", "csharp", "php", "html", "css", "react", "angular"]

palavra_secreta = random.choice(palavras)

letras_adivinhadas = []
tentativas = 6

def exibir_palavra():
    resultado = ""
    for letra in palavra_secreta:
        if letra in letras_adivinhadas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

print("Bem-vindo ao Jogo da Forca!")

while True:
    print(f"\nPalavra: {exibir_palavra()}")
    print(f"Tentativas restantes: {tentativas}")
    
    if exibir_palavra() == palavra_secreta:
        print("\nParabéns, você venceu! A palavra era:", palavra_secreta)
        break

    if tentativas == 0:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)
        break

    letra = input("Adivinhe uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue

    if letra in letras_adivinhadas:
        print("Você já adivinhou essa letra.")
        continue

    letras_adivinhadas.append(letra)

    if letra not in palavra_secreta:
        tentativas -= 1
        print(f"A letra '{letra}' não está na palavra.")
    else:
        print(f"A letra '{letra}' está na palavra!")

print("\nO jogo da forca acabou. Obrigado por jogar!")
