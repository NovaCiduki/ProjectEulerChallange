import sympy

def circle(n: int) -> int:
    string = str(n)
    yield int(string)
    for i in range(len(string) - 1):
        string = string[-1] + string[0:-1]
        yield int(string)

MAX_LENGTH = 1000000
amount = 0
for i in range(MAX_LENGTH):
    if i % 10000 == 0:
        print(f"done with {i/10000}/100")
    if all([sympy.isprime(j) for j in circle(i)]):
        amount += 1
print(f"amount is {amount}")