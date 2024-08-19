print("Bem vindo(a) à Calculadora Simples da Daphene")
numeroa = float(input("Insira o primeiro número: "))
operacao = input("Insira a operação que deseja: ")
numerob = float(input("Insira o segundo número: "))

if operacao == "+":
    resultado = numeroa + numerob
    print("O resultado é: ", resultado)
elif operacao == "-":
    resultado = numeroa - numerob
    print("O resultado é: ", resultado)
elif operacao == "/":
    resultado = numeroa / numerob
    print("O resultado é: ", resultado)
elif operacao == "*":
    resultado = numeroa * numerob
    print("O resultado é: ", resultado)
else: 
    print("Operação inválida")
