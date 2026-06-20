for method in dir(tuple):
    if not method.startswith("__"):
        print(method)


import sys
original = ("apple", "banana", "cherry", "banana", "kiwi", "banana")
print(tuple.__sizeof__(original))
print(sys.getsizeof(original))

s_tuple = original

print(s_tuple)

