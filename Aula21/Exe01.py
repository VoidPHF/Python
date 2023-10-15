nome=input('Digite seu nome:')
idade=input('Escreva sua Idade:')

idade=int(idade)

if nome and idade >= 18:
    print(f"Meu nome é {nome} e eu tenho {idade} anos.")

else:
    print("Desculpe, você não tem idade para entrar.")