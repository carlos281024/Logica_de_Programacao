Salario = float(input("Digite o valor do salário: "))
Emprestimo = float(input("Digite o valor do empréstimo: "))

if Emprestimo <= Salario * 1.3:
    print("O empréstimo pode ser aprovado.")
else:
    if Emprestimo > Salario * 0.3:
        print("O empréstimo não pode ser aprovado.")