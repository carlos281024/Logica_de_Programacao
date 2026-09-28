N = int(input("Digite um número: "))
if N % 3 == 0:
    print("O número é divisível por 3.")
    if N % 7 == 0:
        print("O número é divisível por 7.")
    else:
        if N % 7 == 1 or N % 7 == 2 or N % 7 == 3 or N % 7 == 4 or N % 7 == 5 or N % 7 == 6:
            print("O número não é divisível por 7.")
        else:
            if N % 3 == 1 or N % 3 == 2:
                print("O número não é divisível por 3.")