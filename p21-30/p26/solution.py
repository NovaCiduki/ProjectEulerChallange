def one_div_x(num, dev, x, divs):
    divs.append(dev)
    for i in divs:
        if divs.count(i) > 1:
            return [num, divs]
    # if len(num) > 1000:
    #     return [num, divs]
    # well... very long
    if dev % x == 0:
        num.append(int(dev / x))
        return [num, divs]
    elif dev > x:
        num.append(int(dev / x))
        return one_div_x(num, (dev % x) * 10, x, divs)
    elif dev < x:
        num.append(0)
        return one_div_x(num, dev * 10, x, divs)


def onex(x):
    return one_div_x([], 1, x, [])


def find_loop_dist(arr):
    double = p1 = p2 = -1
    for x in arr:
        if arr.count(x) > 1:
            double = x
    if double == -1:
        # print("no loop")
        return 0
    for i in range(len(arr)):
        if arr[i] == double:
            if p1 == -1:
                p1 = i
            else:
                p2 = i
                return p2 - p1
    print("why im here???")


def find_loop_dist_of_num(x):
    return find_loop_dist(onex(x)[1])


big = [0, 0]
for i in range(2, 1001):
    dist = find_loop_dist_of_num(i)
    print(f"done with {i}/{1000} of the process")
    if dist > big[1]:
        # print("new big")
        # print("i: " + str(i) + ", dist: " + str(dist))
        big[0] = i
        big[1] = dist
print("number,dist of rec loop")
print(big)