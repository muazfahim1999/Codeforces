import itertools
a,b = map(int, input().split())
res = 0

for x in itertools.count(start=0):
    if a*3**x >b*2**x:
        res = x
        break
print(res)
    
