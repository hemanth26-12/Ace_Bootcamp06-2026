for method in dir(list):
    if not method.startswith("__"):
        print(method)

import sys
list = []
print(list.__sizeof__())
print(sys.getsizeof(list))
        