import itertools
n = int(input())
m =[]
res = 0
for x in range (n):
    a = input().split()
    m.append(a)
z = 0
for x in itertools.count(start=0):
    if x == n:
        break
    else:
        z = int(m[x][1]) - int(m[x][0]) + z
        if z > res:
            res = z
        else:
            res = res
    
print(res)
    
