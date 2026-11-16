numero = int(input("Digite um número: "))
print(f"Tabuada do {numero}")
for n in range(1, 11):
    resultado = numero * n
    print(f"{numero} * {n} = {resultado}")