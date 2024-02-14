numbers = [1, 2, 3, 4]
n = 3

powered = list(map(lambda x: x ** n, numbers))

print(numbers, " to the ", n, " power: ", powered)