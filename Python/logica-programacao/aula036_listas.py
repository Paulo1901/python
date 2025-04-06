"""
Listas em Python
Tipo list - mutável
suporta vários valores e qualquer tipo
conhecimento reutilizável - indices e fatiamento
metodos úteis: append, insert pop, del, clear, extend, +
"""

#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)

# lista = list() - Umas das formas de se criar uma lista

# # Criando uma lista com couchetes []

# lista = [] # criando uma lista vazia

# print(type(lista)) # type lista
# print(bool(lista)) # Listas vazia é falsy

# Listas são de tupo mutável, podendo ser mutável

#        0    1      2       3     4
#       -5   -4     -3      -2    -1
lista = [123, True, 'Paulo', 1.2, [456, 'Andreia']]
print(lista[2], type(lista[2])) # checando o tio de dado de dentro da lista

# modicando a lista
lista[-3] = 'Davi' # atribuindo outro valor dentro da lista
print(lista)
