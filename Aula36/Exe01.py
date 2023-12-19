frase = '   Olha só que   , coisa interessante          '
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    lista_frases[i]=lista_frases[i].strip()
print(lista_frases)

""""for i, x in y" é uma estrutura de repetição que itera sobre um objeto iterável,
como uma lista, tupla, dicionário ou conjunto. A cada iteração, 
a variável i recebe o índice do elemento atual no objeto iterável, 
e a variável x recebe o próprio elemento."""