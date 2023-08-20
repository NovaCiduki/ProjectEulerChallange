def t_n(n: int) -> int:
    return int(0.5 * n * (n + 1))

def word_to_number(word: str) -> int:
    """
    turn each letter into the orderd number, sum the numbers.
    """
    return sum((ord(c) - ord('A') + 1 for c in word))

# turn the words into numbers
with open("data.txt", "r") as file_read:
    data = file_read.read()
data = data[:].replace('"', '').split(",")
data = [word_to_number(word) for word in data]
# create list of triangle numbers
n = 2
t_numbers = [1]
while t_numbers[-1] < max(data):
    t_numbers += [t_n(n)]
    n += 1
print(t_numbers)
# counter triangle words:
counter = 0
for word in data:
    if word in t_numbers:
        counter += 1
print(f"total of {counter} triangle words")