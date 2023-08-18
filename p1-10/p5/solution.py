def is_divisible(x):
    for i in range(20):
        if not (x % (i + 1) == 0):
            return False
    return True


def slow():
    ans = 1
    while not (is_divisible(ans)):
        ans += 1
    print(ans)


# for quick solution:
def quick():
    i = 2  # must be divisible by 2
    i *= 3  # must be divisible by 3
    i *= 2  # must be divisible by 4
    i *= 5  # must be divisible by 5
    i *= 1  # must be divisible by 6
    i *= 7  # must be divisible by 7
    i *= 2  # must be divisible by 8
    i *= 3  # must be divisible by 9
    i *= 1  # must be divisible by 10
    i *= 11  # must be divisible by 11
    i *= 1  # must be divisible by 12
    i *= 13  # must be divisible by 13
    i *= 1  # must be divisible by 14
    i *= 1  # must be divisible by 15
    i *= 2  # must be divisible by 16
    i *= 17  # must be divisible by 17
    i *= 1  # must be divisible by 18
    i *= 19  # must be divisible by 19
    t = 1
    while not (is_divisible(t * i)):
        t += 1
    print("t = " + str(t))
    print("t*i = " + str(t * i))

quick()