num = int(input("Digite um número: "))
if num % 3==0:
    print("O número é divisível por 3.")
else:
    if num % 3==1 or num % 3==2:
        print("O número não é divisível por 3.")