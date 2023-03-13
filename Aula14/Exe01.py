primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

condicao1 = primeiro_valor > segundo_valor
condicao2 = primeiro_valor < segundo_valor
condicao3 = primeiro_valor == segundo_valor

if condicao1:
    print(f'O valor {primeiro_valor} é superior ao valor {segundo_valor}.')

elif condicao2:
    print(f'O valor {primeiro_valor} é inferior ao valor {segundo_valor}.')

else:
    print(f'O valor {primeiro_valor} é igual ao valor {segundo_valor}.')
