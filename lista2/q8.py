num = int(input("Digite um número: "))
if num % 5==0:
    print("O número é divisível por 5.")
else:
    if num % 5==1 or num % 5==2 or num % 5==3 or num % 5==4:
        print("O número não é divisível por 5.")