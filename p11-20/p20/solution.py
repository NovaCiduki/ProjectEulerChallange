num = 1
for x in range(1, 100):
    num *= x
num = str(num)
arr = [int(num[i]) for i in range(len(num))]
print(sum(arr))