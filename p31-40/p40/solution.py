"""
d1 will be 1
n <= 9, dn = n
10 <= n <= ???
could be solved manuly...
"""

string = ""
for i in range(0, 1000001):
    string += str(i)
print(string[1], string[10], string[100], string[1000], string[10000], string[100000], string[1000000])
print(int(string[1]) * int(string[10]) * int(string[100]) * int(string[1000]) * int(string[10000]) * int(string[100000]) * int(string[1000000]))