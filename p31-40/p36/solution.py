
def pali_binary(n: int):
    return bin(n)[2:] == bin(n)[2:][::-1]

total_sum = 0
for i in range(1000000):
    if i % 10000 == 0:
        print(f"done with {i/10000}/100")
    if pali_binary(i) and str(i) == str(i)[::-1]:
        total_sum += i
print(f"total sum is {total_sum}")