from functools import reduce

numbers = input("Enter Numbers: ").split()

numbers = list(map(int, numbers))

sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print("Sum: ", sum_of_numbers)