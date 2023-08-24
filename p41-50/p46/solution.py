import math
import sympy

def has_prime_plus_2_square(n: int) -> bool:
    """
    return true if n = prime + 2 * (int ** 2)
    """
    for i in range(0, int(math.sqrt(n)) + 1):
        if sympy.isprime(n - 2 * (i ** 2)):
            print(f"{n} == {int(n - 2 * (i ** 2))} + 2 * ({i} ^ 2)")
            return True
    return False

number = 1
while True:
    if not has_prime_plus_2_square(2 * number + 1):
        print(f"found the number {2 * number + 1}")
        exit()
    number += 1