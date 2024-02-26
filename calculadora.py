nome = str(input("Informe seu nome: "))
print("Olá {} está aqui é um calculadora simples feita em python , veja só!!!".format(nome))

n1 = float(input("Digite qualquer numero: "))
n2 = float(input("Digite outro numero: "))
op = str(input("Qual operação deseja realizar: "))

calc = "sim"

while calc.lower() == "sim":
    if op == "+":
        soma = n1 +n2;
        print(soma)
    elif op == "-":
        sub = n1 - n2;
        print(sub)
    elif op == "*":
        mult = n1 * n2;
        print(mult)
    elif op == "/":
        div = n1/n2;
        print(div)
    else:
        print("Ainda nao aprendemos esse operação :((")
    calc = str(input("Deseja fazer outra operação: "))
    if calc.lower() == "nao" :
        break
    n1 = float(input("Digite qualquer numero: "))
    n2 = float(input("Digite outro numero: "))
    op = str(input("Qual operação deseja realizar"))
