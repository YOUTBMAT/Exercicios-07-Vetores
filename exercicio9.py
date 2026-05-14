numeros = []
negativos = 0
positivos = 0

for i in range(10):
    num = float(input("Digite um número: "))
    numeros.append(num)
for num in numeros:
    if num < 0:
        negativos += 1
    else:
        positivos += num

print(f"Números: {numeros}\nQuantidade de negativos: {negativos}\nSoma positivos: {positivos}")