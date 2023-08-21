import math

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

"""
same like before:
x = h(n)
x = n(2n - 1)
x = 2n^2 - n
2n^2 - n - x = 0
solutions (1 +- sqrt(1 - 4*2*(-x)) / 2*2
1 +- sqrt(1 + 8x) / 4
same like before, "-" can be ingored
n = 1 + sqrt(1 + 8x) / 4
"""
def is_in_h_n(x: int) -> bool:
    return (1 + math.sqrt(1 + 8 * x)) % 4 == 0


def t_n(n: int) -> int:
    return int(n*(n + 1) / 2)

index = 286
while True:
    if is_in_h_n(t_n(index)) and is_in_p_n(t_n(index)):
        print(f"success with index: {index}")
        print(f"triangle number is: {t_n(index)}")
        exit()
    index += 1
