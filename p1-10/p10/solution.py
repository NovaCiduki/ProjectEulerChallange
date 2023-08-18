"""
two slow ways to create prime list,
maybe in java / c this whould be quicker...
"""

def create_primes(until):
    ret = [i for i in range(2, until)]
    index = 0
    while index < len(ret):
        for i in range(2, int(until / ret[index]) + 1):
            if ret.count(ret[index] * i) >= 1:
                ret.remove(ret[index] * i)
        index += 1
    return ret


def create_primes2(until):
    ret = [2]
    num = 3
    flag = True
    while num <= until:
        flag = True
        for i in range(len(ret)):
            if num % (ret[i]) == 0:
                flag = False
        if flag:
            ret.append(num)
        num += 1
    return ret


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


until = 2000000
sum_is = 0
arr = sieveOfEratosthenes(until)
for p in range(2, until + 1):
    if arr[p]:
        sum_is += p
print(sum_is)