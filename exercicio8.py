notas = []

for i in range(15):
    nota = float(input("Digite a nota: "))
    notas.append(nota)

soma = sum(notas)
quantidade = len(notas)
media = soma/quantidade

print(f"Média geral: {media}")