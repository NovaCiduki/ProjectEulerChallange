def factors(x):
    i = 2
    ans = []
    while x > 1:
        if x % i == 0:
            ans.append(i)
            x /= i
        else:
            i += 1
    return ans

print(max(factors(600851475143)))