def d(n):
    tot = 0
    for i in range(1, n):
        if n % i == 0:
            tot += i
    return tot

print("this takes some time...")
numbers = [i for i in range(1, 10001)]
tot = 0
while numbers:
    val = numbers.pop(0)
    d_of = d(val)
    d_of_d = d(d_of)
    if val == d_of_d and val != d_of:
        if numbers.count(d_of) > 0:
            numbers.remove(d_of)
        if val <= 10000:
            tot += val
        if d_of <= 10000:
            tot += d_of
print(tot)