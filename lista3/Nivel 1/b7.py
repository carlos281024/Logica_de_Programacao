positivo = 0
zero = 0
for i in range (6):
    numero = int(input("Digite o numero:"))
    if numero > 0:
        positivo += 1
    elif numero == 0:
        zero += 1
print(positivo, "Positivo")
print(zero, "Zero")
