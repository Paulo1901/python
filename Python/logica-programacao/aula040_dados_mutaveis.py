"""
Cuidado com dados mutáveis
= - copiado o valor (imutavel)
= - aponta para o mesmo valor na memoria (mutável)
"""
lista_a = ['Paulo', 'Andreoa', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'qualquer coisa'
print(lista_a)
print(lista_b)
