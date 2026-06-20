set = {"he-man", "superman", "batman", "spiderman"}
print(set)
print(type(set))
set.add("wonderwoman")
set2 = {"wonderwoman", "flash", "aquaman"}
print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))
set.remove("spiderman")
set.discard("superman")
set.add("supergirl")

print(set)


print(set.isdisjoint(set2))
print(set.issubset(set2))
print(set.issuperset(set2))


for method in dir(set):
    if not method.startswith("__"):
        print(method)