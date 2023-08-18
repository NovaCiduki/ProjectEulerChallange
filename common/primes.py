def is_primt(num: int):
    """
    checks if num is prime
    """
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def sieveOfEratosthenes(num: int):
    """
    this will create list of primes using Sieve of Eratosthenes method.
    :ref: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :param num: create the list of primes until num.
    :return: list with length on num. list[i] will be true iff i is prime.
    """
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    return prime