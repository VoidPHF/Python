Num_Int=input("Digite um número inteiro:" )

#try: Num_Int=int(Num_Int) except: (print("Isso não é um número inteiro"))

Num_Int=int(Num_Int)

condicao1= (Num_Int % 2 == 0)

if condicao1:
    print("Seu número é Par")
    
if not condicao1:
    print("Seu número é Impar")
    

Hora=input("Em que hora você esta lendo isso?:" )

Hora=int(Hora)

Dia= Hora > 0 and Hora <= 11
Tarde= Hora > 11 and Hora <=17
Noite= Hora >=18 and Hora <= 23

if Dia:
    print("Bom Dia")

if Tarde:
    print("Boa Tarde")

if Noite:
    print("Boa Noite")
