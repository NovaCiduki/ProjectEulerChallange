import math

def pandigital(n: int) -> bool:
	"""
    is n a pandigital:
    a * b = n, and a, b, n contains 1 to 9 once.
    """
	for i in range(1, int(math.sqrt(n)) + 1):
		if n % i == 0:
			if "".join(sorted(str(n) + str(i) + str(n // i))) == "123456789":
				return True
	return False


"""
Y can i stop at 10000?
given a, b, c such that a * b = c and those are pandigital, assume c >= 10,000
then c has 5 digits (or more).
so, a and b must have only 4 digits!
biggest product of 2 numbers with 4 digits will be 99 * 99 (checked with script) so
biggest product is 99 * 99 = 9801, but this means:
a * b <= 9,801 < 10,000 <= c
so a * b < c for sure.
this means c can not be bigger then 10,000
"""
print(f"done, total sum is: {sum(i for i in range(1, 10000) if pandigital(i))}")