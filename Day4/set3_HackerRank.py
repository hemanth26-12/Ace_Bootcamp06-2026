d  = int(input())
first = set(map(int, input().split()))

c = int(input())
second = set(map(int, input().split()))    

v1 = first.difference(second)
v2 = second.difference(first)
r = sorted(v1.union(v2))

print(*r, sep = "\n")