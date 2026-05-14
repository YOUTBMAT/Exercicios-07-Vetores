vetor = []

for i in range(10):
    num = int(input("Digite um valor: "))
    vetor.append(num)

maior = max(vetor)
menor = min(vetor)

print(f"Maior: {maior}\nMenor: {menor}")