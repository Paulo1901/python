frase =  'o Python é uma linguagem de programação '\
        'multiparadigma. '\
        'Python foi criado por Guido Van Russunm. '

# Count() para contar qtd da str
# print(frase.count('a'))

i = 0
while i < len(frase):
    letra_atual = frase[i]
    qtd_vezes_letra_apareceu = frase.count(letra_atual)

    print(letra_atual, qtd_vezes_letra_apareceu)
    i += 1
