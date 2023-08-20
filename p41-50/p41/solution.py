import sympy
import itertools

# def is_n_pandigital(number: int):
#     return sorted(str(number)) == sorted(str(i) for i in range(1, len(str(number)) + 1))


# for i in itertools.permutations:
solution = 0
string = ""
for digit in range(1, 10):
    string += str(digit)
    for perm in itertools.permutations(string):
        number = int("".join(perm))
        if sympy.isprime(number) and number > solution:
            solution = number

print(f"the solution is {solution}")
