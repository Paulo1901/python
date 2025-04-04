"""
Iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue se iterador
"""

# for letra in texto

texto = ('Paulo') # iterável
iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
print()
for letra in texto:
    print(letra)

# o metodo __next__() entrega o proximo valor
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(texto.__next__())
# print(next(texto))
# iter('Paulo') # __iter__()

# numeros = range(0, 100, 8)

# for numero in numeros:
#     print(numero)
