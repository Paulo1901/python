"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não (tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
v2 = 'b'
# print(id(v1))
# print(id(v2))

condição = True
passou_no_if = None

if condição:
  passou_no_if = True # bandeira
  print('Faça algo')
else:
  print('Não faça algo.')

# print(passou_no_if, passou_no_if is None) # checa se passou no if é None
# print(passou_no_if, passou_no_if is not None) # checa se passou no if não é None

if passou_no_if is None:
  print('Não passou no if')
else:
  print('Passou no if') 
