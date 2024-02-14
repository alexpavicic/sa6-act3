people = ["Alice", "Bob", "Charlie", "Amy"]

sorted_people = sorted(people, key=lambda x: (len(x), x))

print(sorted_people)
