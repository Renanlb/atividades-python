def calcular_media(notas):
    if len(notas) == 0:
        return 0
    soma = sum(notas)
    media = soma / len(notas)
    return media

def determinar_nota(media):
    if media >= 90:
        return 'A'
    elif media >= 80:
        return 'B'
    elif media >= 70:
        return 'C'
    elif media >= 60:
        return 'D'
    else:
        return 'F'

notas = []
num_notas = int(input("Quantas notas você deseja inserir? "))

for i in range(num_notas):
    nota = float(input(f"Insira a nota {i + 1}: "))
    notas.append(nota)

media = calcular_media(notas)

nota_correspondente = determinar_nota(media)

print(f"A média das notas é: {media}")
print(f"A nota correspondente é: {nota_correspondente}")