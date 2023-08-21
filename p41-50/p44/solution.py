import math
def p_n(n: int) -> int:
    return int(n * (3 * n - 1) / 2)

"""
given a x we want to check if there is n such that p(n) = x,
if so, there is such n that:
x = p(n) ---->
x = (3(n**2) - n) / 2 ---->
2x = 3n^2 - n ---->
3n^2 - n - 2x = 0 ---->
quadratic formula is (-b +- sqrt(-b - 4ac)) / 2a
solutions = (1 +- sqrt((-1)^2 - 4*3*(-2x)) / 2*3 ---->
solutions = (1 +- sqrt(1 + 24x)) / 6
min(x) is 1, so min(1 + 24x) is 5, so 
1 +- 5 = 6 or -4, we can see that the "-" can be ignored.
so, solution = 1 + sqrt(1 + 24x) / 6 = n
this means that if (1 + sqrt(1 + 24x) / 6) is integer, then we have such n
"""
def is_in_p_n(x: int) -> bool:
    return (1 + math.sqrt(1 + 24 * x)) % 6 == 0

val1 = 2
while True:
    for val2 in range(1, val1):
        if is_in_p_n(p_n(val1) + p_n(val2)) and is_in_p_n(abs(p_n(val1) - p_n(val2))):
            print(f"got solution ({val1}, {val2}).")
            print(f"p_n(val1) + p_n(val2) == {p_n(val1) + p_n(val2)}")
            print(f"|p_n(val1) - p_n(val2)| == {abs(p_n(val1) - p_n(val2))}")
            exit()
    val1 += 1