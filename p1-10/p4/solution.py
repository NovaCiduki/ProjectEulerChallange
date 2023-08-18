max_a = 0
max_b = 0
max_ab = 0
for a in range(1000):
    for b in range(1000):
        if int(str(a * b)[::-1]) == a * b:
            if a * b > max_ab:
                max_a = a
                max_b = b
                max_ab = a * b
print("max_a = " + str(max_a))
print("max_b = " + str(max_b))
print("max_ab = " + str(max_ab))