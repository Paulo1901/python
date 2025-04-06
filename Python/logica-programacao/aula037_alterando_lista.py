"""
Listas em Python
Tipo list - mutável
suporta vários valores e qualquer tipo
conhecimento reutilizável - indices e fatiamento
metodos úteis: 
    append, insert pop, del, clear, extend, +
criar, ler, alterar, apagar = lista[i] (CRUD)

Obs: o interresante da lista é remover e adicionar
no final da lista, nunca é aconselhavel remover do meio da lista
por motivos de processamento.
"""

#        0   1   2   3   4   5 - postivos
#       -6  -5  -4  -3  -2  -1 - negativos
lista = [10, 20, 30, 40, 50, 60]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(70) # adicionando valor na lista
lista.pop() # removendo o utimo elemento da lista
print(lista)
utilmo_valor = lista.pop()
print(lista, 'Removendo,', utilmo_valor)
outro_valor_removido = lista.pop(2)
print(lista, 'removido da lista,', outro_valor_removido)
