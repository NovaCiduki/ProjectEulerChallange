import math

# this will make this function to remember calcs, it will take memory, but will make the calc faster.
# @functools.cache
def count_distinct_prime_factors(n):
	count = 0
	while n > 1:
		count += 1
		for i in range(2, int(math.sqrt(n) + 1)):
			if n % i == 0:
				while True:
					n //= i
					if n % i != 0:
						break
				break
        # n is prime on this else
		else:
			break
	return count

COUNT = 4
for i in range(2, 1000000):
	arr = [count_distinct_prime_factors(i + x) == COUNT for x in range(COUNT)]
	if all(arr):
		print(f"solution is {i}")
		exit()