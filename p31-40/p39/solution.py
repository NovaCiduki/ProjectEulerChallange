def number_of_solutions(p: int) -> list:
    options = []
    for a in range(1, p):
        for b in range(a, p):
            c = p - b - a
            if (a ** 2 + b ** 2) == (c ** 2):
                options += [sorted([a, b, c])]
    return options

# print(number_of_solutions(120))

max_solutions = []
max_p = 0
for p in range(1, 1001):
    if p % 10 == 0:
        print(f"done with {p/10}/100")
    temp = number_of_solutions(p)
    if len(temp) > len(max_solutions):
        max_solutions = temp
        max_p = p
print(f"the max solutions is {max_solutions}, with p of: {max_p}")