def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


number = 1
index = 0
while index < 10001:
    number += 1
    if is_prime(number):
        index += 1
        print("prime = " + str(number) + ", index = " + str(index))