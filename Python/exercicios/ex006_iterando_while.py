"""
Iterando uma string
"""

nome = 'Paulo Carvalho' 
nome2 = 'Andreia Carvalho'

indice = 0 # criando um indice que incia com zero
novo_nme = '' # criado uma string vazia
while indice < len(nome): # enquanto indice for < que o tamanho do nome "condição"
    letra = nome[indice] # criado a variavel letra que recebe nome[indice]
    novo_nme += letra # a varavel novo_nome recebe a iteração de letra por letra até o tamanho do nome for maior
    indice += 1 

indice_2 = 0
novo_nome_2 = ''
while indice_2 < len(nome2):
    letra_2 = nome2[indice_2]
    novo_nome_2 += letra_2
    indice_2 += 1

print(novo_nome_2, end='')
print()
print(novo_nme, end='')


