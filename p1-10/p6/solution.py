sum_of_squares = 0
square_of_sum = 0
for i in range(100):
    sum_of_squares += (i + 1) * (i + 1)
    square_of_sum += (i+1)
square_of_sum = square_of_sum*square_of_sum
print(square_of_sum-sum_of_squares)