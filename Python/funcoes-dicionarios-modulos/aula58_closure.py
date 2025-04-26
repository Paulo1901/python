# closure e função que retornam outra funções

def criar_saudacao(saudacao):
	def saudar(nome):
		return f'{saudacao}, {nome}'
	return saudar

Falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Bom noite')
print(Falar_bom_dia('Paulo'))
print(falar_boa_noite('Andreia'))

print()
for nome in ['Andreia', 'Paulo', 'Davi']:
	print(Falar_bom_dia(nome))
	print(falar_boa_noite(nome))
	