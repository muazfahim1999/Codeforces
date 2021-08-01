import itertools
n = int(input())
m = []
res = 0
for x in range(n):
    m.append(input())
for x in itertools.count(start=1):
    if x == n:
        break
    else:
        if m[x] != m[x-1]:
            res += 1

print(res+1)
