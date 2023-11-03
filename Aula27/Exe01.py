# Calculadora
while True:
    print("Bem-Vindo a calculadora em PYTHON")
    valor_1=float(input("Digite um número: "))
    valor_2=float(input("Digite outro número: "))
    op1=input("Qual operação deseja fazer? +, -, /, *, **: ")

    numeros_validos=None    
    try:
        numeros_validos=True
    except:
        numeros_validos=None
        
    if numeros_validos is None:
        print("Digite os numeros corretamente")
        continue
        
    if op1 == '+':
        print(valor_1 + valor_2)
    if op1 == '-':
        print(valor_1 - valor_2)
    if op1 == '/':
        print(valor_1 / valor_2)
    if op1 == '*':
        print(valor_1 * valor_2)
    if op1 == '**':
        print(valor_1**valor_2)
        
    sair = input('Deseja sair?: ').lower().startswith('s')
    if sair is True:
        break
    continue
#Codigos pra usar mais tarde "algo.lower()" deixa tudo em minusculo
#algo.startswith('algum caracter') significa que se começa com tal caracter, realiza oq vc digitar abaixo disso
    