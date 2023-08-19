def number_to_human_string(x):
    # don = dict of number
    don = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        1000: "one thousand"
    }
    one = x % 10
    ten = x % 100 - one
    hundred = x % 1000 - ten - one
    if 0 <= x <= 19:
        return don[x]
    elif 20 <= x <= 99:
        if one == 0:
            return don[ten]
        else:
            return don[ten] + " " + don[one]
    else:
        hundred_num = int(hundred / 100)
        hundred_string = don[hundred_num] + " " + don[100]
        if x == 1000:
            return don[1000]
        elif one == 0 or ten == 0:
            if one == 0 and ten == 0:
                return hundred_string
            elif one == 0 and ten != 0:
                return hundred_string + " and " + don[ten]
            else:
                return hundred_string + " and " + don[one]
        return hundred_string + " and " + number_to_human_string(x % 100)


tot = 0
for x in range(1, 1001):
    tot += len(number_to_human_string(x).replace(" ", ""))
print(tot)

# about 10 min' lost due to writing "thousand" instead of "one thousand"