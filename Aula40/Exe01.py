frase= str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A apareceu {frase.count('A')} vezes na frase')
print(f'A primeira apareceu na posição  {frase.find('A')+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind('A')+1}')

frase_dividida= frase.split()
print(f'A primeira palavra é {frase_dividida[0]}')
print(f'A ultima palavra é{frase_dividida[len(frase_dividida)-1]}')