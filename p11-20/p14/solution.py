MAX_LENGTH = 1000000

def length(x):
    if x % (MAX_LENGTH // 10) == 0:
        print(f"you are {x // 100000}/10 of the way")
    count = 1
    while x != 1:
        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
        count += 1
    return count


print("this will take some time...")
arr = [length(x) for x in range(1, MAX_LENGTH + 1)]
maximum = 0
index = 0
for x in range(MAX_LENGTH):
    if arr[x] > maximum:
        maximum = arr[x]
        index = x
print("the answer: " + str(index + 1))
print("chain length: " + str(maximum))