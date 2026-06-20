
import copy

for method  in dir(range):
    if not method.startswith("__"):
        print(method)


rate = range(5)

print(range.__sizeof__(rate))

ll = [10, [13, 14], 18, 22]

ss = copy.copy(ll)
dd = copy.deepcopy(ll)
dd[2] = 100
ss[1].append(5)
print(ll)
print(ss)
print(ll)
print(dd)