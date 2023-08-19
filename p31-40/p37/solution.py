import sympy

def get_parts_of_number(n: int) -> int:
    """
    this will yield one after another parts of the number by cutting the number from right,
    and then from the left.
    for example, with input of 3797 this will return:
    3797, 3, 37, 379, 797, 97, 7
    """
    length = len(str(n))
    yield n
    # cut from the left
    curr = str(n)
    for i in range(1, length):
        yield int(curr[:i])
    for i in range(1, length):
        yield int(curr[i:])
    

counter = 0
# 2, 3, 5, 7 does not count
number = 10
total_sum = 0
while counter < 11:
    if all([sympy.isprime(i) for i in get_parts_of_number(number)]):
        counter += 1
        print(f"found {counter}/11, the new added number is: {number}")
        total_sum += number
    number += 1
print(f"total sum is: {total_sum}")