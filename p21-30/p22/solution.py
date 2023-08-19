import data

dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
              "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
              "X": 24, "Y": 25, "Z": 26}


def name_to_num(name):
    re = 0
    for let in name:
        re += dictionary[let]
    return re


names = data.NAMES
names.sort()
ans = 0
for i in range(len(names)):
    ans += (name_to_num(names[i]) * (i + 1))
print(ans)
