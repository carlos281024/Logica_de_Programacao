Numero = int(input("Digite um número: "))
Raiz = Numero ** (1/2)
Quadrado = Numero ** 2
if Numero >= 0:
    print("A raiz quadrada do número é: ", Raiz)
else:
    if Numero < 0:
        print("Quadrado do número é: ", Quadrado)