import itertools
n = int(input())
x = set((input().split())[1:])
y = set((input().split())[1:])
t = x.union(y)
t.discard('0')
if len(t) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
