# Calculadora
print("Bem-Vindo a calculadora em PYTHON")

valor1=float(input("Digite um numero: "))
while valor1=='':
    input("Valor invalido, digite novamente: ")
    continue
if valor1 != '':
    op1=input("Qual operação deseja fazer? +, -, /, *, **: ")
    
    valor2=float(input("Digite outro numero: "))
    
    if op1 == '+':
        print(valor1 + valor2)
    if op1 == '-':
        print(valor1 - valor2)
    if op1 == '/':
        print(valor1 / valor2)
    if op1 == '*':
        print(valor1 * valor2)
    if op1 == '**':
        print(valor1**valor2)
    