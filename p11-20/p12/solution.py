def nth_triangle_number(n: int) -> int:
    """
    get the n'th triangle number: 1 + 2 + 3 + ... + n
    """
    return (n * (n + 1)) / 2

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

i = 1
while True:
    print(f"i is: {i}")
    if get_divisors_amount(nth_triangle_number(i)) > 500:
        print(f"done with i: {i}. number is: {nth_triangle_number(i)}")
        break
    i += 1