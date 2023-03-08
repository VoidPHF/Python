# Calculadora de IMC

nome = 'Paulo Henrique'
altura = 1.80
peso = 70
imc = peso / (altura * altura)

print(nome, 'tem', altura, 'de altura, ' 'pesa', peso,
      'quilos e tem seu IMC de', imc, sep=' ', end=' ')

linha_1 = f'{nome} tem {altura:.1f} de altura'
print(linha_1)
# ... isso se chama elipsia, e funciona como placeholder, assim o codigo não da erro
