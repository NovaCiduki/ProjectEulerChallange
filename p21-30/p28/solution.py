def a_(n):
    return 2 * n - 1


def b_(n):
    if n == 1:
        return 1
    return 8 * n - 8


def c_(n):
    if n == 1:
        return 1
    else:
        return c_(n - 1) + b_(n - 1)


def d_(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        finish_of_last = c_(n) - 1
        right_down = finish_of_last + a_(n) - 1
        left_down = right_down + a_(n) - 1
        left_up = left_down + a_(n) - 1
        right_up = left_up + a_(n) - 1
        return right_up + right_down + left_down + left_up


tot = 0
for n in range(502):
    print(f"done with {n}/501 of the way")
    tot += d_(n)
print(tot)