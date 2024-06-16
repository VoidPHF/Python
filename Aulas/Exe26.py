nome=input("Diga seu nome: ")
indice=0
tamanho_nome= len(nome)
novo=''
while indice < tamanho_nome:     
    letra=(nome[indice])
    novo += f'*{letra}'
    indice+=1
    print(novo)
    continue
