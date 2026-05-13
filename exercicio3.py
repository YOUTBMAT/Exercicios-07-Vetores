vetorA = []
vetorB = []
contador = 0

while contador < 10:
    numeroReal = float(input("Digite um número real: "))
    vetorA.append(numeroReal)

    potencia = numeroReal**2
    vetorB.append(potencia)

    contador += 1

print (vetorA)
print (vetorB)