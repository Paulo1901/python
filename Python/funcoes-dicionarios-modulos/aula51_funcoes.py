"""
Introdução às funções (def) em python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código
elas podem reber valores por parâmetros (argumentos)
e retornando um valor especificado.
Por padrão, funções Python retorna None (nada).
"""

# def imprimir(a, b, c): # recebendo parâmtros a, b, c na função
#     print(a, b, c)

# imprimir(1, 2, 3) # executandoa função "passando os argumentos (valores)"
# imprimir(4, 5, 6)

def saudacao(nome='Está sem nome'):
    print(f'ola, {nome}')

saudacao('Paulo Carvalho')
saudacao('Andreia Carvalho')
saudacao('Davi Carvalho')
saudacao()
