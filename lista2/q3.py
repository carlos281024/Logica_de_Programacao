numero = int(input("Digite um número: "))
par_impar = numero % 2
if par_impar == 0:
    print("O número é par.")
else:
    if par_impar == 1:
        print("O número é ímpar.")