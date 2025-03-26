"""
Fatiamento de strings
 012345678
 ola mundo
-987654321
Fatiamento [i:f:p] [::]
obs: a função len torna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[-4]) # pegando apena uma letra
print(variavel[2:8]) # fatiamento em Python em fatamento o utimo valor é omitido, temos sempre que pegar mais 1
print(variavel[1:]) # para se pega todo lista basta obtir o final
print(variavel[:5])

# Fatiamento negativos
print(variavel[-8:-1])
print(variavel[-1])

# função len
print(len(variavel))

# Fatiamento com passo, escolhendo de quanto você pode pular
print(variavel[0:9:2])
print(variavel[::-1]) # invertendo string com fatiamento
