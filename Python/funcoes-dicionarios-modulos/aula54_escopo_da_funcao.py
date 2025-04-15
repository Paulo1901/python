"""
Escopo da função em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
O escopo global é o espaço onde todo o código é alcansavél 
O escopo local é o escopo onde apenas nomes do mesmo local 
podem acessar
"""

x = 1 # Global variable

def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2

        print(x, y)

    outra_funcao()
    # x = 1 # variable do escopo da função
    print(x)


print(x)
escopo()
print(x)