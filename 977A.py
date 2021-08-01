import itertools
n,k = map(int, input().split())
m = str(n)
for x in itertools.count(start=0):
    if x == k:
        break
    else:
        if m[-1] == '0':
            m = m[:-1]
        else:
            m = int(m)-1
            m= str(m)
        
print(m)
        
