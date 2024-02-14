def find_max(numbers, compare):

    max_num = numbers[0]  

    for num in numbers:
        if compare(num, max_num) > 0:  
            max_num = num
    return max_num

numbers = [5, 3, 7, 1, 7, 2]
compare = lambda x, y: x > y

max_num = find_max(numbers, compare)

print("Maximum number:", max_num)
