for a in range(10, 100):
    for b in range(10, 100):
        if a / b >= 1:
            continue
        set_a = set(str(a))
        set_b = set(str(b))
        intersection = set_a.intersection(set_b)
        if len(intersection) == 1:
            set_a = set_a.difference(intersection)
            set_b = set_b.difference(intersection)
            if intersection.pop() == '0':
                continue
            if len(set_a) > 0 and len(set_b) > 0:
                val_a = int(set_a.pop())
                val_b = int(set_b.pop())
                if val_b != 0:
                    if val_a / val_b == a / b:
                        print(f"one of the 4 fractions is: ({a}, {b})")
"""
output will be:
one of the 4 fractions is: (16, 64)
one of the 4 fractions is: (19, 95)
one of the 4 fractions is: (26, 65)
one of the 4 fractions is: (49, 98)
16/64 == 1/4
19/95 == 1/5
26/65 == 2/5
49/98 == 4/8 == 1/2
1/4 * 1/5 * 2/5 * 1/2 == 1*1*2*1/4*5*5*2 == 1/4*5*5 == 1/100
so 100 is the solution!
"""
