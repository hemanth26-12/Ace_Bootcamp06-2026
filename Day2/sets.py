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