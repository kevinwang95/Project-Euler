''' This is a solution to Project Euler Problem 1, "Multiples of 3 and 5". The problem is below:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_multiples(number):
	total_sum = 0
	for i in range (1, 1000):
			if i % 3 == 0 or i % 5 == 0:
				total_sum += i
	return total_sum

print sum_multiples(1000)	
