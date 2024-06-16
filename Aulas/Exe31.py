palavra_secreta = 'perfume'
letras_acertadas = ''
num_tent=0

while True:

    letra_digitada = input('Digite uma letra: ')
    num_tent += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
        print("Palavra formada: ", palavra_formada)
        
    if palavra_formada==palavra_secreta:
        print("VOCÊ GANHOOU!!")
        print("A palavra era", palavra_secreta)
        print("Tentativas: ", num_tent)