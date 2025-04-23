# Function exercises

# Create a function that multiplies all the unnamed arguments
# given.
# Return the total to a variable and display the value
# of the variable.

def multiplication(*args):
	total = 1 # creating a variable to receive the total of the sum
	for number in args:
		total *= number
	return total 

multiply = multiplication(1, 2, 3, 4, 5)
print(multiply)

# Create a function that returns false if a number is even or odd
# returns whether the number is even or odd

def even_or_odd(num):
	multiple_of_two = num % 2 == 0

	if multiple_of_two:
		return f'{num} e par'
	else:
		return f'{num} e impar'

print(even_or_odd(10))
print(even_or_odd(7))
print(even_or_odd(8))
