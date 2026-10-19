nome = input("Digite o nome do cliente: ")
codigo = int(input("Digite o código do lanche: "))
bebida = input("Deseja bebida?(sim/nao) ")
recebimento = int(input("Digite o código do recebimento: " ))
aluno = input("É aluno? (sim/nao): ")
if codigo == 1:
    preco = 18.00
    nome_lanche = "hambúrguer"
elif codigo == 2:
    preco = 12.00
    nome_lanche = "hot dog"
elif codigo == 3:
    preco = 15.00
    nome_lanche = "açaí"
else: 
    print("codigo invalido")
    preco = 0.00
    nome_lanche = "invalido" 
if bebida == "sim":
    preco == preco + 6.00
if recebimento == 1:
    preco = preco + 8.00
    entrega_ok = "sim"
else:
    entrega_ok = "nao"
if aluno == "sim":
    preco = preco * 0.90
print("==============================")
print(f"Cliente: {nome}")
print(f"Lanche: {nome_lanche}")
print(f"Bebida: {bebida}")
print(f"Entrega: {entrega_ok}")
print(f"Total a pagar: R$ {preco: 2F}")
print("==============================")