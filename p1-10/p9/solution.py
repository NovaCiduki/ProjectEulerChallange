print("this takes some time...")
for a in range(1, 1001):
    for b in range(a, 1001):
        for c in range(b, 1001):
            if a * a + b * b == c * c:
                if a + b + c == 1000:
                    print("a: " + str(a))
                    print("b: " + str(b))
                    print("c: " + str(c))
                    print("abc: " + str(a * b * c))