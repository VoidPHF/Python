# Calculadora de IMC

nome = 'Paulo Henrique'
altura = 1.80
peso = 70
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, ' 'pesa', peso,
      'quilos e tem seu IMC de', imc, sep=' ', end=' ')
# ... isso se chama elipsia, e funciona como placeholder, assim o codigo não da erro

# Introdução breve a Fstring, que possibilita a criação de variaveis dentro de uma string
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
