def get_divisors(n: int) -> dict:
    """
    return the divisors on the number n.
    for e.x.
    get_divisors(9000) will return {2:3, 3:2, 5:3}
    becuase (2 ** 3) * (3 ** 2) * (5 ** 3) == 9000
    """
    i = 2
    dict_return = {}
    while n > 1:
        if n % i == 0:
            if i in dict_return:
                dict_return[i] += 1
            else:
                dict_return[i] = 1
            n //= i
        else:
            i += 1
    return dict_return

def get_divisors_amount(n: int) -> int:
    """
    return the amount of divisors of a numebr n
    """
    amount = 1
    divisors = get_divisors(n)
    for i in divisors:
        amount *= (divisors[i] + 1)
    return amount

import math

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