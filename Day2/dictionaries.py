c = {"name": "John", "age": 30, "city": "New York"  }
print(c["name"])
print(c["age"])
c["age"] = 31
print(c)
c["country"] = "INDIA"
print(c)
del c["city"]
print(c)
print(c.values())
print(c.keys())
print(c.items())
c.fromkeys(["name", "age", "city"], "unknown")
print(c)
