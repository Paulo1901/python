"""
Higher Order Functions
funções de primeira classe
"""

def greeting(msg):
	return f'{msg}, {name}'


def execute(function, *args):
	return function(*args)

print(execute(greeting, 'Good morning', 'Paulo'))

# value = greeting('Bom dia!')
# print(value)