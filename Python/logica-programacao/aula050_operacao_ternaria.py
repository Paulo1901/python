# Operação ternária (condicional de uma linha)
# <valor> if <condição> else <outro valor>

# Ex: 
variavel_true = 'valor' if True else 'outro valor'
variavel_false = 'valor' if False else 'outro valor'

print(variavel_true)
print(variavel_false)

condicao = 10 == 11 # criado condição
variavel = 'valor' if condicao else 'outro valor' # checando com operação ternária
print(variavel)

digito = 9 # digito > 9 = 0
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

