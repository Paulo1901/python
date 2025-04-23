"""
Higher Order Functions
funções de primeira classe
"""

def greeting(msg):
	return f'{msg}, {name}'


def execute(function, msg):
	return function(msg)

v = execute(greeting, 'Good morning')
print(v)

# value = greeting('Bom dia!')
# print(value)