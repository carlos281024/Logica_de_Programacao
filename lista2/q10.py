A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
if A > B:
    print("O Maior valor é A.")
    print("O Menor valor é B.")
else:
    if A < B:
        print("O Maior valor é B.")
        print("O Menor valor é A.")
    else:
        if A == B:
            print("Os valores são iguais.")