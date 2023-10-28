Num_Int=input("Digite um número inteiro: " )

Num_Int=int(Num_Int)

condicao1= (Num_Int % 2 == 0)

if condicao1:
    print("Seu número é Par")
    
if not condicao1:
    print("Seu número é Impar")
    

Hora=input("Em que hora você esta lendo isso?: " )

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

Nome=input("Qual seu primeiro nome?: ")

if Nome >= 



"""Maneira do Professor:

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# except:
#     print('Você não digitou um número inteiro')

------------------------

entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

-----------------

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

"""