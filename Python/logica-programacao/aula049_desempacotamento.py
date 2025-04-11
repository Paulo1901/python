# Desempacotamento em chamadas
# de métodos e fuções
string = 'ABC'
lista = ['Paulo', 'Andreia', 1, 2, 3, 'Davi']
tupla = 'python', 'é', 'legal'

salas = [
#     0        1     
    ['Paulo', 'Andreia', ], # 0
#     0     
    ['Fabiana'], # 1
#     0       1       2
    ['Luiz', 'João', 'Eduardo'] # 2
]

# a, b, *_, c = lista
# print(a, c)


# Utilizando um for para percorrer a lista
for nome in lista: 
    print(nome, end=' ')

# a mesma coisa que for esta fazendo
print('Paulo', 'Andreia', 1, 2, 3, 'Davi')

# desenpacotando a lista
print(*lista)

# desempacotando a string
print(*string)

# desempacotando a tupla
print(*tupla)

###############################################

print(salas)
# desempacotando sala
print(*salas, sep='\n') # mostrando a lista de forma mais simples
