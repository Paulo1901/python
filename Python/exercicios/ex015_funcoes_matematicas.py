# Exercicios
# Crie funções que duplique, triplique e quadriplique
# o número recebido como parâmetro 

# possiveis soluções
# def duplicar(num):
# 	return num * 2

# def triplicar(num):
# 	return num * 3

# def quadriplicar(num):
# 	return num * 4


# print(duplicar(2))
# print(triplicar(2))
# print(quadriplicar(2))

# Melhor soluçao desse problema

def criar_multiplicador(multiplicador):
	def multiplicar(num):
		return num * multiplicador
	return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
