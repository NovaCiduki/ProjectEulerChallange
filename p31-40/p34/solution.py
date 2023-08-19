import math

def factorial_digit_sum(n: int):
    return sum(math.factorial(int(i)) for i in str(n)) == n


MAX_LENGTH = 10000000
"""
can we stop at 10,000,000?
say that a number has 8 digits, minimum number with 8 digits is 10,000,000
now, 9! * 8 = 2,903,040 < 10,000,000
so there is no n > 10,000,000 that would return true from factorial_digit_sum...
"""
ITERATION = MAX_LENGTH / 100
numbers_with_attribute = []
for i in range(3, MAX_LENGTH):
    if i % ITERATION == 0:
        print(f"done with {i/100000}/{MAX_LENGTH/100000} of the way")
    if factorial_digit_sum(i):
        numbers_with_attribute += [i]
print(f"numbers with attribute are: {numbers_with_attribute}")
print(f"total sum is: {sum(numbers_with_attribute)}")