import itertools

def check_property(string: str) -> bool:
    condits = [
        int(string[1:4]) % 2 == 0,
        int(string[2:5]) % 3 == 0,
        int(string[3:6]) % 5 == 0,
        int(string[4:7]) % 7 == 0,
        int(string[5:8]) % 11 == 0,
        int(string[6:9]) % 13 == 0,
        int(string[7:10]) % 17 == 0,
    ]
    return all(condits)

print("this takes some time...")
total_sum = 0
for perm in itertools.permutations("0123456789"):
    string = "".join(perm)
    if check_property(string):
        total_sum += int(string)
print(f"total sum is: {total_sum}")