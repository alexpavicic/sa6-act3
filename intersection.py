list1 = [1, 2, 3, 4]
list2 = [2, 5, 4, 6]

intersection = list(filter(lambda x: x in list1, list2))

print("Intersection: ", intersection)