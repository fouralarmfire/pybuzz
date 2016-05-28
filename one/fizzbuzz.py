def by_three(num):
	return check_divisible(num, 3)

def by_five(num):
	return check_divisible(num, 5)

def by_fifteen(num):
	return check_divisible(num, 15)

def check_divisible(number, divisor):
	if number % divisor == 0:
		return True

def says(num):
	if by_fifteen(num):
		return 'fizzbuzz'
	if by_three(num):
		return 'fizz'
	if by_five(num):
		return 'buzz'
	else:
		return num