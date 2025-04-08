"""
Exercicio
exiba os indices da lista
"""

lista = ['Paulo', 'Andreia', 'Davi']
indices = range(len(lista)) # criou-se uma variavel que pegou os indices do tamanho da lista

print(lista)
print(indices)

for indice in indices: # iterando sobre os indices
    print(indice, lista[indice], type(lista[indice])) # imprindo as posições dos indices e e seus valores
    
