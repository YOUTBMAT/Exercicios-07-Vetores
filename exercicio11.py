valores = [13,45,87,4,9]

maior = max(valores)
menor = min(valores)

posicaoMaior = valores.index(maior)
posicaoMenor = valores.index(menor)

print(f"Valores: {valores}\nMaior: {maior}\nMenor: {menor}\nPosição maior: {posicaoMaior}\nPosição menor: {posicaoMenor}")