import math


def fibo(n):
    return int((1 / math.sqrt(5)) * ((((1 + math.sqrt(5)) / 2) ** n) - (((1 - math.sqrt(5)) / 2) ** n)))


a = 1
b = 1
c = 0
index = 2
while len(str(c)) < 1000:
    c = a + b
    index += 1
    a = b
    b = c
print(index)
