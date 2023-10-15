nome=input('Digite seu nome:')
idade=input('Escreva sua Idade:')

idade=int(idade)
emon=nome[::-1]
encontrar=(" ")
letraUM=nome[0]
UltimaLetra=nome[-1]
if nome and idade >= 18:
    print(f"Meu nome é {nome} e eu tenho {idade} anos.")
    print(f"Seu nome invertido é {emon}")
    if ' ' in nome:
        print('Seu nome tem espaço')
    else:
        print('Seu nome não tem espaço')
    print(f"A primeira letra do seu nome é:{letraUM}")
    print(f"A ultima letra do seu nome é {UltimaLetra}")

else:
    print("Desculpe, você não tem idade para entrar.")
    
#   print(len(variavel [-6:])