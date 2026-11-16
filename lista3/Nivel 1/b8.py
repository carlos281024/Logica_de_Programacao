Idade_Valida = 0
Idade_Invalida = 0
for i in range(5):
    idade = int(input("Digite a idade: "))
    if idade >= 16:
        Idade_Valida += 1
print(Idade_Valida, "Idade Valida")