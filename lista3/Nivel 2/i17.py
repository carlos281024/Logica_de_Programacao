soma = 0
qntd = 0
for vez in range (5):
    nota = int(input("Nota: "))
    soma = soma + nota
    media = soma / 5
    if nota >= 6:
        qntd += 1
print (f"Sua média é {media}")
print (qntd, "maior ou igual á 6")