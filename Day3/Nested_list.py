'''import copy
list = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
list1 = copy.copy(list)
list1[0][0] = 100
list2 = copy.deepcopy(list)
print("Original List:", list)
print("Shallow Copy:", list1)



list2[0][2] = 10

print("Original List:", list)
print("Deep Copy:", list2)'''
list3 = [[0]*3 for _ in range(3)]
print("List3:", list3)
list3[0][0] = 5
print("List3:", list3)
