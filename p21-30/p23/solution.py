def perfect_abundant_or_deficient(n):
    divisors_sum = 0
    for devs in range(1, n):
        if n % devs == 0:
            divisors_sum += devs
    if divisors_sum == n:
        return 0  # "perfect"
    elif divisors_sum > n:
        return 1  # "abundant"
    else:
        return 2  # "deficient"


def abundant():
    arr = []
    for x in range(1, 28123):
        if perfect_abundant_or_deficient(x) == 1:
            arr.append(x)
    return arr


print("takes about 1 min...")
abundant_numbers = abundant()
sum_of_2 = [False for x in range(28123)]
for val1 in abundant_numbers:
    for val2 in abundant_numbers:
        val3 = val1 + val2
        if val3 < 28123:
            sum_of_2[val3] = True

tot = 0
i = 0
length = len(sum_of_2)
while i < length:
    if not sum_of_2[i]:
        tot += i
    i += 1
print(tot)