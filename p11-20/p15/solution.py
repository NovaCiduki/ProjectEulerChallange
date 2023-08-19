def nCr(n, k):
    n2 = 1
    k2 = 1
    n_k = 1
    for x in range(n):
        n2 *= (x + 1)
    for x in range(k):
        k2 *= (x + 1)
    for x in range(n - k):
        n_k *= (x + 1)
    return int(n2 / (k2 * n_k))

print(nCr(40, 20))
# nCr(40, 20) is actually a math solution, you can calc this on calculator.