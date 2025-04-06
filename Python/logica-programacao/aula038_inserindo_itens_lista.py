# Inserindo qualquer valor no indice da lista
# adicionando valor (append)

lista = [10, 20, 30, 40]
lista.append('Paulo') # inserindo item ao final da lista
nome = lista.pop()
print(lista, nome) # removendo o utimo item da lista

lista.append(1223)
del lista[-1] # deletando o valore da lista pelo indice -1 
# lista.clear() limpando a lista

lista.insert(100, 5) # inserindo valor na lista pelo indice

# erro causado quando tentamos acessar um indice na lista que nãe existe
# IndexError: list index out of range
print(lista[4])
