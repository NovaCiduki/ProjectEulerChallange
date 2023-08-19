def is_prime(n):
    if n <= 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_amount(a, b):
    n = 0
    while is_prime(n ** 2 + a * n + b):
        n += 1
    return n


maximum_primes = 0
max_a = 0
max_b = 0
for a in range(-999, 1000):
    print(f"done with {a + 1001}/2000 of the way")
    for b in range(-1000, 1001):
        amount = prime_amount(a, b)
        if amount > maximum_primes:
            maximum_primes = amount
            max_a = a
            max_b = b
print(maximum_primes, max_a, max_b)
print(max_a * max_b)