soma=0
multiplicador=10
cpf='10854392408'
for i in range(len(cpf)):
    if i<=8:
        print(cpf[i])
        soma=int(cpf[i])*multiplicador+soma
        multiplicador=multiplicador-1  
dez_vez= soma*10
resto=dez_vez%11
if resto > 9:
    resultado=0
else:
    resultado = resto

print(soma)
print(resultado)
print(dez_vez)