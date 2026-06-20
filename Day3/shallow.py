my_list = [1, 2, 3, 4, 5]

shallow_copy = my_list

shallow_copy[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]
print(shallow_copy)  # Output: [10, 2, 3, 4, 5]
