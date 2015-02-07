''' This is my solution to Project Euler Problem 2, which asks to find the sum of the even number Fibonacci numbers up to 4 million.
'''

''' The function is_even returns a boolean and determines whether or not a number is even.'''
def is_even(number):
	if number % 2 == 0:
		return True
	else:
		return False


''' The function fibonacci returns the nth fibonacci term, where n is the number in the sequence. The function uses the recursive definition of the 
fibonacci sequence as the sum of the two previous terms. '''
def fibonacci(n):
	if n == 0:
		return 1
	if n == 1:
		return 2
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

''' The function sum_fibonacci sums up all the even terms of the fibonacci sequence less than a maximum number, and returns that sum'''
def sum_fibonacci(max):
	n = 0
	sum = 0
	while fibonacci(n) < max:
		if is_even(fibonacci(n)):
			sum += fibonacci(n)
		n = n + 1	
	return sum

sum_fibonacci(4000000)