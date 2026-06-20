original = [1, 2, 3, 4, 5]
deep_copy = original[:]

deep_copy[2] = 24
print(original)   
print(deep_copy)  # Output: [1, 2, 24,'''

import copy

for method in dir(copy):
    if not method.startswith("__"):
        if not method.startswith("_"):
             print(method)

    