vetor = [1,2,3,4,5,6,7,8,9,10]

quantidade = 0

for i in vetor:
    if i % 2 == 0:
        print (i)
        quantidade += 1

print(f"Quantidade de números pares: {quantidade}")