nome = str(input("Qual é seu nome completo?")).strip()
print(f'Seu nome tem silva? {nome}')
if 'silva' in nome.lower():
    print('Oi, Silva')
else:
    print('Não tem Silva')