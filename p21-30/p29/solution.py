start = 2
end = 101
arr = []
for a in range(start, end):
    for b in range(start, end):
        num = a ** b
        if arr.count(num) == 0:
            arr.append(num)
print(len(arr))