# While/else recurso peculiar da linguagem
string = 'Paulo Carvalho'

i = 0 # Criado um indice 
while i < len(string): # checando se indice é menor que o tamanho da string
    letra = string[i] 

    if letra == ' ': # checando se espaço a letra
        break

    print(letra)
    i += 1
else:
    print('Está dentro do while')
print('Está fora do while')
